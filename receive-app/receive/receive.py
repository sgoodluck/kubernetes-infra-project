import paho.mqtt.client as mqtt
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, message):
    logging.info("Received message: " + str(message.payload.decode("utf-8")))

broker_address = "broker-app"
broker_port = 1883
topic = "hello_world/broadcast"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.protocol_version = mqtt.MQTTv5

client.connect(broker_address, broker_port)

try:
    client.loop_forever()

except KeyboardInterrupt:
    logging.info("Stopping the receiver...")

except Exception as e:
    logging.error(f"Exception occurred: {str(e)}")

finally:
    client.disconnect()
