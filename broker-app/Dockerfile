# Use image for mosquitto
FROM eclipse-mosquitto:2.0.18

# Copy the config file
COPY mosquitto.conf /mosquitto/config/mosquitto.conf

# Expose MQTT port and MQTT Websocket Port
EXPOSE 1883 9001

# Start Mosquitto when container starts
CMD ["mosquitto", "-c", "/mosquitto/config/mosquitto.conf"]
