from typing import Optional

from ha_mqtt_discovery import sanitize_name
from ha_mqtt_discovery.base_sensor import BaseSensor
from ha_mqtt_discovery.device import Device


class Sensor(BaseSensor):
    def __init__(
            self,
            device: Device,
            name: str,
            device_class: Optional[str],
            unit_of_measurement: Optional[str],
            value_template: str,
            sensor_id: str = None,
            precision: Optional[int] = None,
            state_topic: str = None,
            unique_id: str = None,
            state_class: str = 'measurement'
    ):
        super().__init__('sensor')
        self.device = device
        self.name = name
        self.sensor_id = sensor_id or sanitize_name(name)
        self.base_topic = self.device.sensor_topic(self.sensor_id)
        self.state_topic = state_topic or f'{self.base_topic}'
        self.unique_id = unique_id or self.device.unique_id(self.sensor_id)
        self.device_class = device_class
        self.unit_of_measurement = unit_of_measurement
        self.value_template = value_template
        self.precision = precision
        self.state_class = state_class
        self.device.register(self)

    def build(self) -> dict:
        return self.build_base({
            'state_class': self.state_class,
            'state_topic': self.state_topic,
            'suggested_display_precision': self.precision,
            'unit_of_measurement': self.unit_of_measurement,
            'value_template': self.value_template,
        })