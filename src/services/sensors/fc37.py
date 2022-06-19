from .influx_sensor import InfluxSensor

class FC37(InfluxSensor):
  _measurement = 'weather station'
  _fields = ['rain']
