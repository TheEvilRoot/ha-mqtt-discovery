from ha_mqtt_discovery import sanitize_name
from ha_mqtt_discovery.base_sensor import BaseSensor
from ha_mqtt_discovery.device import Device


class Switch(BaseSensor):
    def __init__(
            self,
            device: Device,
            name: str,
            sensor_id: str = None,
            state_topic: str = None,
            cmd_topic: str = None,
            unique_id: str = None,
            optimistic: bool = True,
            payload_on: str = None,
            payload_off: str = None,
            state_on: str = None,
            state_off: str = None,
    ):
        super().__init__('switch')
        self.device = device
        self.name = name
        self.sensor_id = sensor_id or sanitize_name(name)
        self.base_topic = self.device.sensor_topic(self.sensor_id)
        self.cmd_topic = cmd_topic or f'{self.base_topic}/set'
        self.state_topic = state_topic or f'{self.base_topic}/state'
        self.unique_id = unique_id or self.device.unique_id(self.sensor_id)
        self.optimistic = optimistic
        self.payload_on = payload_on or 'on'
        self.payload_off = payload_off or 'off'
        self.state_on = state_on or 'on'
        self.state_off = state_off or 'off'
        self.device.register(self)

    def build(self):
        return self.build_base({
            'payload_on': self.payload_on,
            'payload_off': self.payload_off,
            'state_on': self.state_on,
            'state_off': self.state_off,
            'state_topic': self.state_topic,
            'command_topic': self.cmd_topic,
        })
