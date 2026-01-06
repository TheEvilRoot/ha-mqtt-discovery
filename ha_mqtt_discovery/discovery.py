
class Discovery:
    def __init__(self, base_topic: str):
        self.base_topic = base_topic
        self.name = 'ha_mqtt_discovery'
        self.version = '1.2.0'
        self.url = 'https://github.com/TheEvilRoot/ha-mqtt-discovery'
        self.base_discovery_topic = 'homeassistant'
        self.device = None

    def build(self):
        return {
            'dev': {
                'name': self.device.name,
                'model': self.device.model,
                'model_id': self.device.model_id,
                'identifiers': [self.device.device_id]
            },
            'o': { 'name': self.name, 'sw': self.version, 'url': self.url },
            'cmps': self.device.build()
        }

    def discovery_topic(self, device_id: str = None) -> str:
        if device_id is None:
            assert self.device is not None
            device_id = self.device.device_id
        return f'{self.base_discovery_topic}/device/{device_id}/config'

    def device_topic(self, device_id: str) -> str:
        return f'{self.base_topic}/{device_id}'

    def register(self, device: "Device"):
        self.device = device
