from ha_mqtt_discovery import sanitize_name
from ha_mqtt_discovery.base_sensor import BaseSensor
from ha_mqtt_discovery.device import Device


class Lock(BaseSensor):
    def __init__(
            self,
            device: Device,
            name: str,
            sensor_id: str = None,
            cmd_topic: str = None,
            state_topic: str = None,
            cmd_template: str = None,
            code_format: str = None,
            optimistic: bool = True,
            retain: bool = True,
            unique_id: str = None
    ):
        super().__init__('lock')
        self.device = device
        self.name = name
        self.sensor_id = sensor_id or sanitize_name(name)
        self.base_topic = self.device.sensor_topic(self.sensor_id)
        self.cmd_topic = cmd_topic or f'{self.base_topic}/set'
        self.state_topic = state_topic or f'{self.base_topic}/state'
        self.unique_id = unique_id or self.device.unique_id(self.sensor_id)
        self.cmd_template = cmd_template
        self.code_format = code_format
        self.optimistic = optimistic
        self.retain = retain
        self.device.register(self)

    def build(self) -> dict:
        return self.build_base({
            'command_topic': self.cmd_topic,
            'state_topic': self.state_topic,
            'optimistic': self.optimistic,
            'code_format': self.code_format,
            'retain': self.retain,
            'command_template': self.cmd_template
        })