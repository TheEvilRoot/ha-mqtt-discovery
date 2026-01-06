import datetime
import json
import os
import time

if __name__ == '__main__':
    from paho.mqtt.client import Client
    from ha_mqtt_discovery import Discovery, Device, Button

    discovery = Discovery('sample')
    discovery.name = 'test'
    device = Device(discovery, 'Sample Device', 'sample_device', 'Sample Model', 'sample_model_id')
    button = Button(device, 'Identify', device_class='identify')

    client = Client()
    if os.environ.get('MQTT_USER'):
        client.username_pw_set(os.environ.get('MQTT_USER'), os.environ.get('MQTT_PASSWORD'))

    def on_message(c, u, message):
        print(f'Received message: {message.topic} {message.payload}')

    client.on_message = on_message
    client.connect(os.environ.get('MQTT_HOST', 'localhost'), 1883)
    client.loop_start()
    client.publish(discovery.discovery_topic(), json.dumps(discovery.build()))
    client.subscribe(button.cmd_topic)

    while True:
        time.sleep(10)


