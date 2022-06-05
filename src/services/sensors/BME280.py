from Sensor import Sensor

class BME280(Sensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['temperature', 'humidity', 'athmosphere pressure', 'altitude']
