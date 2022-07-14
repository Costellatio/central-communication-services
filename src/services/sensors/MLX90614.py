from .InfluxSensor import InfluxSensor

class MLX90614(InfluxSensor):
  MEASUREMENT = 'weather station'
  FIELDS = ['difference (ambient - object) temp']