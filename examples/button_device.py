import datetime
import json
import os
import time

if __name__ == '__main__':
    from paho.mqtt.client import Client
    from ha_mqtt_discovery import DiscoveryConfig

    discovery = DiscoveryConfig('sample', 'sample')
    discovery.device('Sample device', 'Model', 'sample_device')
    discovery.origin('sample', '1.0.0', 'http://example.com')
    discovery.button(name='Identify',
                     sensor_id='button_identify',
                     device_class='identify')

    client = Client()
    if os.environ.get('MQTT_USER'):
        client.username_pw_set(os.environ.get('MQTT_USER'), os.environ.get('MQTT_PASSWORD'))

    def on_message(client, userdata, message):
        print(f'Received message: {message.topic} {message.payload}')


    client.on_message = on_message
    client.connect(os.environ.get('MQTT_HOST', 'localhost'), 1883)
    client.loop_start()
    client.publish(discovery.topic, json.dumps(discovery.build()))
    client.subscribe(discovery.command_topic_of('button_identify'))

    while True:
        time.sleep(10)


