# ha-mqtt-discovery

Simple library to dynamically create MQTT discovery configuration 
for Home Assistant and use it for publishing sensor data to MQTT broker.

It provides simple to use interface to setup device, origin and component configurations 
with JSON output. Use helper functions like `sensor()`, `switch()`, etc to add
components to discovery config.

### Api coverage

> Currently, all coverage described below is partial

- [ ] Alarm control panel
- [ ] Binary sensor
- [x] Button
- [ ] Camera
- [ ] Cover
- [ ] Climate (HVAC)
- [ ] Device tracker
- [ ] Device trigger
- [ ] Event
- [ ] Fan
- [ ] Humidifier
- [ ] Image
- [ ] Lawn mower
- [ ] Light
- [x] Lock
- [ ] Notify
- [ ] Number
- [ ] Scene
- [ ] Select
- [x] Sensor
- [ ] Siren
- [ ] Switch
- [ ] Update
- [ ] Tag scanner
- [ ] Text
- [ ] Vacuum
- [ ] Valve
- [ ] Water heater

### Example:
```python
discovery_config = DiscoveryConfig('server_1', 'mqstats')
discovery_config.device('Server 1', 'Mac Mini M1', 'mac_mini_m1')
discovery_config.origin('mqstats', '1.1', 'https://github.com/TheEvilRoot/mqstats')
discovery_config.sensor(name='CPU%',
                        device_class=None,
                        unit_of_measurement='%',
                        value_template='{{ value_json.cpu_percent | round(1) }}',
                        sensor_id='cpu_percent',
                        state_class='measurement',
                        precision=1)
discovery_config.sensor(name='CPU Frequency',
                        device_class='frequency',
                        unit_of_measurement='Mhz',
                        value_template='{{ value_json.cpu_freq | int }}',
                        sensor_id='cpu_percent',
                        state_class='measurement',
                        precision=0)
# ...
send_message(client, discovery_config.state_topic_of('cpu_percent'), {'cpu_percent': cpu_percent})
```

### Install

You can install package from git or locally cloned repository directory

```shell
pip3 install git+https://github.com/TheEvilRoot/ha-mqtt-discovery
# or 
git clone https://github.com/TheEvilRoot/ha-mqtt-discovery 
pip3 install ./ha-mqtt-discovery
```