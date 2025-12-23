import json
import random
import time
from datetime import datetime
import paho.mqtt.client as mqtt

BROKER_HOST = "localhost"
BROKER_PORT = 1883
TOPIC = "sensor/temperature"
PUBLISH_INTERVAL_SECONDS = 1.0

def generate_temperature():
    base = 25.0
    noise = random.uniform(-2.0, 2.0)
    return round(base + noise, 2)

def main():
    client = mqtt.Client()
    client.connect(BROKER_HOST, BROKER_PORT, 60)
    client.loop_start()
    try:
        while True:
            payload = {
                "temperature": generate_temperature(),
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }
            client.publish(TOPIC, json.dumps(payload))
            time.sleep(PUBLISH_INTERVAL_SECONDS)
    except KeyboardInterrupt:
        pass
    finally:
        client.loop_stop()
        client.disconnect()

if __name__ == "__main__":
    main()
