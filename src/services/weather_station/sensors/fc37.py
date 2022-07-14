from .sensor import Sensor

class FC37(Sensor):
  _measurement = 'weather station'
  _fields = ['rain']
