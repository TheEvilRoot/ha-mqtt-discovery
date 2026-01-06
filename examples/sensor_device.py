import json
import os
import random
import time

if __name__ == '__main__':
    from paho.mqtt.client import Client
    from ha_mqtt_discovery import Discovery, Device, Sensor

    discovery = Discovery('sample')
    device = Device(discovery, 'Sample Sensor', 'sample_sensor', 'Sample Model', 'sample_model')
    sensor = Sensor(
        device,
        name='Value',
        device_class='temperature',
        unit_of_measurement='°C',
        value_template='{{ value | int }}',
        precision=0,
        state_class='measurement'
    )

    client = Client()
    if os.environ.get('MQTT_USER'):
        client.username_pw_set(os.environ.get('MQTT_USER'), os.environ.get('MQTT_PASSWORD'))
    client.connect(os.environ.get('MQTT_HOST', 'localhost'), 1883)
    client.publish(discovery.discovery_topic(), json.dumps(discovery.build()))
    client.loop_start()

    value = 0
    while True:
        value = value + random.randint(-5, 5)
        client.publish(sensor.state_topic, str(value))
        print(f'Sensor value: {value}')
        time.sleep(3)

