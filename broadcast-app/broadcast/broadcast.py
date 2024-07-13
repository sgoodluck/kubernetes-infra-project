import paho.mqtt.client as mqtt
import time
import random

broker_address = "mosquitto-broker"
topic = "hello_world/broadcast"

client = mqtt.Client("Broadcast", protocol=mqtt.MQTTv5)
client.connect(broker_address)

message = "Hello world"

while True:
    wait_time = random.uniform(1, 10)
    time.sleep(wait_time)
    client.publish(topic, message)
