class BaseSensor:
    def __init__(self, platform: str):
        self.name = None
        self.device_class = None
        self.platform = platform
        self.sensor_id = None
        self.unique_id = None

    def build_base(self, d: dict) -> dict:
        return {
            'name': self.name,
            'platform': self.platform,
            'device_class': self.device_class,
            'unique_id': self.unique_id,
            **d
        }
