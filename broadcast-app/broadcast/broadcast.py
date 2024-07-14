import paho.mqtt.client as mqtt
import time
import random
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f"Connected with result code {rc}")

def on_publish(client, userdata, mid, properties=None, reasonCode=None):
    logging.info(f"Message {mid} published")

broker_address = "broker-app"
broker_port = 1883
topic = "hello_world/broadcast"
message = "Hello world"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish
client.protocol_version = mqtt.MQTTv5

try:
    client.connect(broker_address, broker_port)
    logging.info("Connected to MQTT broker")
    client.loop_start()

    while True:
        wait_time = random.uniform(1, 10)
        time.sleep(wait_time)
        result = client.publish(topic, message)
        result.wait_for_publish()
        logging.info(f"Published {message} to topic {topic}")

except Exception as e:
    logging.error(f"Failed to connect or publish message: {e}")

finally:
    client.loop_stop()
    client.disconnect()
    logging.info("Disconnected from MQTT broker")
