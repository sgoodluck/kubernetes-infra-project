import paho.mqtt.client as mqtt
import time
import random

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")

def on_publish(client, userdata, mid, properties=None):
    print(f"Message {mid} published")

broker_address = "test.mosquitto.org"
topic = "hello_world/broadcast"
message = "Hello world"

client = mqtt.Client(client_id="Broadcast", protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_publish = on_publish

client.connect(broker_address)
client.loop_start()

while True:
    wait_time = random.uniform(1, 10)
    time.sleep(wait_time)
    result = client.publish(topic, message)
    result.wait_for_publish()

client.loop_stop()
