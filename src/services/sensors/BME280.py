from .InfluxSensor import InfluxSensor

class BME280(InfluxSensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['temperature', 'humidity', 'athmosphere pressure', 'altitude']
