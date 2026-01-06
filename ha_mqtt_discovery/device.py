from ha_mqtt_discovery.utils import sanitize_name
from ha_mqtt_discovery.base_sensor import BaseSensor
from ha_mqtt_discovery.discovery import Discovery


class Device:
    def __init__(self, discovery: Discovery, name: str, device_id: str, model: str, model_id: str = None):
        self.name = name
        self.model = model
        self.model_id = model_id or sanitize_name(name)
        self.discovery = discovery
        self.device_id = sanitize_name(device_id)
        self.base_topic = self.discovery.device_topic(self.device_id)
        self.discovery_topic = self.discovery.discovery_topic(self.device_id)
        self.sensors = {}
        self.discovery.register(self)

    def build(self) -> dict:
        return {k: v.build() for k, v in self.sensors.items()}

    def sensor_topic(self, sensor_id: str) -> str:
        return f'{self.base_topic}/{sensor_id}'

    def unique_id(self, sensor_id: str) -> str:
        return f'{self.device_id}/{sensor_id}'

    def register(self, sensor: BaseSensor):
        self.sensors[sensor.sensor_id] = sensor
