from .influx_sensor import InfluxSensor

class BME280(InfluxSensor):
  _measurement = 'weather station'
  _fields = ['temperature', 'humidity', 'athmosphere pressure', 'altitude']
