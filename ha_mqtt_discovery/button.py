from ha_mqtt_discovery.base_sensor import BaseSensor
from ha_mqtt_discovery.device import Device
from ha_mqtt_discovery.utils import sanitize_name

class Button(BaseSensor):
    def __init__(
            self,
            device: Device,
            name: str,
            sensor_id: str = None,
            cmd_topic: str = None,
            device_class: str = None,
            payload_press: str = None,
            retain: bool = False,
            unique_id: str = None
    ):
        super().__init__('button')
        self.device = device
        self.name = name
        self.sensor_id = sensor_id or sanitize_name(self.name)
        self.base_topic = self.device.sensor_topic(self.sensor_id)
        self.cmd_topic = cmd_topic or f'{self.base_topic}/set'
        self.unique_id = unique_id or self.device.unique_id(self.sensor_id)
        self.payload_press = payload_press or 'PRESS'
        self.device_class = device_class
        self.retain = retain
        self.device.register(self)

    def build(self) -> dict:
        return self.build_base({
            'command_topic': self.cmd_topic,
            'payload_press': self.payload_press,
            'retain': self.retain,
        })
