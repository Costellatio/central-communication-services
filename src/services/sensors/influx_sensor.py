from .sensor import Sensor

class InfluxSensor(Sensor):
  _measurement = None
  _fields = None

  def process(self, properties):
    if self._measurement == None:
      raise Exception('Uninitialized measurement constant')

    if self._fields == None:
      raise Exception('Uninitialized fields constant')

    if len(self._fields) != len(properties):
      raise Exception('Mismatching properties and fields lengths')

    return {
      'measurement': self._measurement,
      'fields': list(zip(self._fields, properties))
    }
