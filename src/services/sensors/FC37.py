from .InfluxSensor import InfluxSensor

class FC37(InfluxSensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['rain']
