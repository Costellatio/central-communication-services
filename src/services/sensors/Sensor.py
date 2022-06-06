class Sensor:
  MEASUREMENT = None
  FIELDS = None

  def process(self, properties):
    if self.__class__.__name__ == 'Sensor':
      raise Exception('Undefined behaviour. Class interface method `process` called')

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
