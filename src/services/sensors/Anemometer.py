from .Sensor import Sensor

class Anemometer(Sensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['wind speed']
