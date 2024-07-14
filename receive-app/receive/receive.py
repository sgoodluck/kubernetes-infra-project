import paho.mqtt.client as mqtt
import logging
from flask import Flask, render_template

# Init Logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Init flask app and array to store messages
app = Flask(__name__)
received_messages = []

# Init Settings
BROKER_ADDRESS = "broker-app"
BROKER_PORT = 1883
TOPIC = "hello_world/broadcast"

# Init mqtt callback functions
def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, message):
    logging.info("Received message: " + str(message.payload.decode("utf-8")))
    # Append received message to global list
    received_messages.append(str(message.payload.decode("utf-8")))


# Configure MQTT and Connect
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.protocol_version = mqtt.MQTTv5

client.connect(BROKER_ADDRESS, BROKER_PORT)

try:
    client.loop_start()

    # Render index.html
    @app.route('/')
    def index():
        return render_template('index.html', messages=received_messages)

    # Run flask app
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)

except KeyboardInterrupt:
    logging.info("Stopping the receiver...")

except Exception as e:
    logging.error(f"Exception occurred: {str(e)}")

finally:
    client.loop_stop() 
    client.disconnect()
