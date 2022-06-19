from .sensor import Sensor

class Anemometer(Sensor):
  _measurement = 'weather station'
  _fields = ['wind speed']
