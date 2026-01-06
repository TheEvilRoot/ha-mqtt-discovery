# ha-mqtt-discovery

Simple library to dynamically create MQTT discovery configuration 
for Home Assistant and use it for publishing sensor data to MQTT broker.

It provides simple to use interface to setup device, origin and component configurations 
with JSON output. 

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

See examples in [examples](examples) folder...

### Install

You can install package from git or locally cloned repository directory

```shell
pip3 install git+https://github.com/TheEvilRoot/ha-mqtt-discovery
# or 
git clone https://github.com/TheEvilRoot/ha-mqtt-discovery 
pip3 install ./ha-mqtt-discovery
```