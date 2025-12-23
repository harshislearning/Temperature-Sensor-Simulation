import json
import threading
import queue
from flask import Flask, render_template
from flask_sock import Sock
import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
MQTT_TOPIC = "sensor/temperature"

app = Flask(__name__)
sock = Sock(app)

latest_queue = queue.Queue(maxsize=100)
ws_clients = set()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(MQTT_TOPIC)
    else:
        print("MQTT connection failed with code", rc)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        if "temperature" in data and "timestamp" in data:
            if latest_queue.full():
                latest_queue.get()
            latest_queue.put(data)
            for ws in list(ws_clients):
                try:
                    ws.send(json.dumps(data))
                except Exception:
                    ws_clients.discard(ws)
    except json.JSONDecodeError:
        print("Malformed JSON in dashboard")

def mqtt_listener():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_forever()

@app.route("/")
def index():
    return render_template("index.html")

@sock.route("/ws")
def ws_route(ws):
    ws_clients.add(ws)
    try:
        while True:
            _ = ws.receive()
    except Exception:
        pass
    finally:
        ws_clients.discard(ws)

def start_mqtt_thread():
    t = threading.Thread(target=mqtt_listener, daemon=True)
    t.start()

if __name__ == "__main__":
    start_mqtt_thread()
    app.run(host="0.0.0.0", port=5000, debug=True)
