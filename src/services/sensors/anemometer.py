from .influx_sensor import InfluxSensor

class Anemometer(InfluxSensor):
  _measurement = 'weather station'
  _fields = ['wind speed']
