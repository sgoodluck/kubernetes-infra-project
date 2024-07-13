import paho.mqtt.client as mqtt

broker_address = "test.mosquitto.org"
topic = "test/topic"

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))

client = mqtt.Client(client_id="Receive", protocol=mqtt.MQTTv5)
client.connect(broker_address)
client.subscribe(topic)
client.on_message = on_message

client.loop_forever()
