import paho.mqtt.client as mqtt
import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# Init logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Init Settings
BROKER_ADDRESS = "broker-app"
BROKER_PORT = 1883
TOPIC = "hello_world/broadcast"

# Init flask app, SocketIO, and array to store messages
app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")
received_messages = []

# Init mqtt callback functions
def on_connect(client, userdata, flags, rc, properties=None):
    logging.info(f"Connected with result code {rc}")
    client.subscribe(TOPIC)

def on_message(client, userdata, message):
    decoded_message = str(message.payload.decode("utf-8"))
    logging.info(f"Received message: {decoded_message}")
    received_messages.append(decoded_message)
    socketio.emit('new_message', {'message': decoded_message}, namespace='/')

# Configure mqtt
client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message
client.protocol_version = mqtt.MQTTv5

try:
    client.connect(BROKER_ADDRESS, BROKER_PORT)
    client.loop_start()

    # Render index.html at root
    @app.route('/')
    def index():
        return render_template('index.html', messages=received_messages)

    # Run flask app with SocketIO and allow unsafe for non-production
    if __name__ == '__main__':
        socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)

except KeyboardInterrupt:
    logging.info("Stopping the receiver...")

except Exception as e:
    logging.error(f"Exception occurred: {str(e)}")

finally:
    client.loop_stop()
    client.disconnect()
    logging.info("Disconnected from MQTT broker")
