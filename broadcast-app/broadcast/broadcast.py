import paho.mqtt.client as mqtt
import time
import random
import logging

# Init logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define mqtt constants
BROKER_ADDRESS = "broker-app"
BROKER_PORT = 1883
TOPIC = "hello_world/broadcast"
MESSAGE = "Hello world"

# Setup functions for mqtt
def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f"Connected to broker with result code {rc}")

def on_publish(client, userdata, mid, properties=None, reasonCode=None):
    logging.info(f"Message {mid} published")

# Configure mqtt
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish
client.protocol_version = mqtt.MQTTv5

try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    client.loop_start()

    while True:
        wait_time = random.uniform(1, 10)
        time.sleep(wait_time)
        result = client.publish(TOPIC, MESSAGE)
        result.wait_for_publish()
        logging.info(f"Published {MESSAGE} to topic {TOPIC}")

except KeyboardInterrupt:
    logging.info("Stopping the broadcaster...")

except Exception as e:
    logging.error(f"Failed to connect or publish message: {e}")

finally:
    client.loop_stop()
    client.disconnect()
    logging.info("Disconnected from MQTT broker")
