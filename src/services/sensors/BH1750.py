from .InfluxSensor import InfluxSensor

class BH1750(InfluxSensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['light level']