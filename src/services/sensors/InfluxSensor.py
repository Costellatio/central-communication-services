from .Sensor import Sensor

class InfluxSensor(Sensor):
  MEASUREMENT = None
  FIELDS = None

  def process(self, properties):
    if self.MEASUREMENT == None:
      raise Exception('Uninitialized measurement constant')

    if self.FIELDS == None:
      raise Exception('Uninitialized fields constant')

    if len(self.FIELDS) != len(properties):
      raise Exception('Mismatching properties and fields lengths')

    return {
      'measurement': self.MEASUREMENT,
      'fields': list(zip(self.FIELDS, properties))
    }
