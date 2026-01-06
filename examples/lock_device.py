import datetime
import json
import os
import time

if __name__ == '__main__':
    from paho.mqtt.client import Client
    from ha_mqtt_discovery import Discovery, Device, Lock

    discovery = Discovery('sample')
    device = Device(discovery, 'Sample Device', 'sample_device', 'Sample Model', 'sample_model')
    lock = Lock(device, 'Lock', code_format='^\\d{4}$',
                cmd_template='{ "action": "{{ value }}", "code":"{{ code }}" }')

    client = Client()
    if os.environ.get('MQTT_USER'):
        client.username_pw_set(os.environ.get('MQTT_USER'), os.environ.get('MQTT_PASSWORD'))


    lock_state = 'LOCKED'
    def on_message(client, u, message):
        global lock_state
        print(f'Received message: {message.topic} {message.payload}')
        if message.topic == lock.cmd_topic:
            request = json.loads(message.payload.decode())
            code = request['code']
            action = request['action']
            code_valid = code == '1122'
            if not code_valid:
                print(f'Invalid code: {code}')
                client.publish(lock.state_topic, lock_state)
                return
            if action == 'LOCK':
                lock_state = 'LOCKED'
                client.publish(lock.state_topic, lock_state)
            elif action == 'UNLOCK':
                lock_state = 'UNLOCKED'
                client.publish(lock.state_topic, lock_state)

    client.on_message = on_message
    client.connect(os.environ.get('MQTT_HOST', 'localhost'), 1883)
    client.loop_start()
    client.publish(discovery.discovery_topic(), json.dumps(discovery.build()))
    client.subscribe(lock.cmd_topic)

    while True:
        time.sleep(10)


