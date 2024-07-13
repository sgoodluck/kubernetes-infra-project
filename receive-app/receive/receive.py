import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc, properties=None):
    print(f"Connected with result code {rc}")
    client.subscribe(topic)

def on_message(client, userdata, message):
    print("Received message: " + str(message.payload.decode("utf-8")))

broker_address = "broker-service"
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
    print("Stopping the receiver...")

finally:
    client.disconnect()
