from .InfluxSensor import InfluxSensor

class Anemometer(InfluxSensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['wind speed']
