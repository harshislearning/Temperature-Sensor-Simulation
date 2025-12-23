import json
import threading
import queue
import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
MQTT_TOPIC = "sensor/temperature"
ROS2_TOPIC = "/temperature/data"

message_queue = queue.Queue()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(MQTT_TOPIC)
    else:
        print("MQTT connection failed with code", rc)

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode("utf-8"))
        if "temperature" in data and "timestamp" in data:
            bridged = {
                "topic": ROS2_TOPIC,
                "temperature": data["temperature"],
                "timestamp": data["timestamp"]
            }
            message_queue.put(bridged)
        else:
            print("Malformed JSON (missing keys)")
    except json.JSONDecodeError:
        print("Malformed JSON (decode error)")

def mqtt_thread():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    while True:
        try:
            client.connect(BROKER_HOST, BROKER_PORT, 60)
            client.loop_forever()
        except Exception as e:
            print("MQTT disconnect/error:", e)
            time.sleep(2)

def ros2_simulator_thread():
    while True:
        bridged = message_queue.get()
        print(f"[ROS2 node] Topic: {bridged['topic']}, "
              f"Temp: {bridged['temperature']} C, "
              f"Timestamp: {bridged['timestamp']}")

def main():
    t1 = threading.Thread(target=mqtt_thread, daemon=True)
    t2 = threading.Thread(target=ros2_simulator_thread, daemon=True)
    t1.start()
    t2.start()
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("Bridge stopped.")

if __name__ == "__main__":
    import time
    main()
