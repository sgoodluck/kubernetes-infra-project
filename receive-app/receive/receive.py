import paho.mqtt.client as mqtt

broker_address = "localhost"
broker_port = 1883
topic = "hello_world/broadcast"

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))

client = mqtt.Client(client_id="Receive", protocol=mqtt.MQTTv5)
client.connect(broker_address, broker_port)
client.subscribe(topic)
client.on_message = on_message

client.loop_forever()
