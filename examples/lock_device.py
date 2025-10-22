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
    discovery.lock(name='Lock',
                   sensor_id='simple_lock',
                   code_format='^\\d{4}$',
                   cmd_template='{ "action": "{{ value }}", "code":"{{ code }}" }')

    client = Client()
    if os.environ.get('MQTT_USER'):
        client.username_pw_set(os.environ.get('MQTT_USER'), os.environ.get('MQTT_PASSWORD'))


    lock_state = 'LOCKED'
    def on_message(client, userdata, message):
        global lock_state
        print(f'Received message: {message.topic} {message.payload}')
        if message.topic == discovery.command_topic_of('simple_lock'):
            request = json.loads(message.payload.decode())
            code = request['code']
            action = request['action']
            code_valid = code == '1122'
            if not code_valid:
                print(f'Invalid code: {code}')
                client.publish(discovery.state_topic_of('simple_lock'), lock_state)
                return
            if action == 'LOCK':
                lock_state = 'LOCKED'
                client.publish(discovery.state_topic_of('simple_lock'), lock_state)
            elif action == 'UNLOCK':
                lock_state = 'UNLOCKED'
                client.publish(discovery.state_topic_of('simple_lock'), lock_state)

    client.on_message = on_message
    client.connect(os.environ.get('MQTT_HOST', 'localhost'), 1883)
    client.loop_start()
    client.publish(discovery.topic, json.dumps(discovery.build()))
    client.subscribe(discovery.command_topic_of('simple_lock'))

    while True:
        time.sleep(10)


