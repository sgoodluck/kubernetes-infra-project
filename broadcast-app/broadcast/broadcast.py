import paho.mqtt.client as mqtt
import time
import random

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

def on_publish(client, userdata, mid, properties=None, reasonCode=None):
    print(f"Message {mid} published")

broker_address = "localhost"
broker_port = 1883
topic = "hello_world/broadcast"
message = "Hello world"

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_publish = on_publish
client.protocol_version = mqtt.MQTTv5

client.connect(broker_address, broker_port)
client.loop_start()

try:
    while True:
        wait_time = random.uniform(1, 10)
        time.sleep(wait_time)
        result = client.publish(topic, message)
        result.wait_for_publish()

except KeyboardInterrupt:
    print("Stopping the broadcast...")

finally:
    client.loop_stop()
    client.disconnect()
