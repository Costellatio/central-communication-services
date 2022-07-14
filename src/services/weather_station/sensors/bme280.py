from .sensor import Sensor

class BME280(Sensor):
  _measurement = 'weather station'
  _fields = ['temperature', 'humidity', 'athmosphere pressure', 'altitude']
