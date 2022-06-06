from .Sensor import Sensor

class FC37(Sensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['rain']
