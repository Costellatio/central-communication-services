class Sensor:
  _measurement = None
  _fields = None

  @classmethod
  def process(klass, properties):
    if klass._measurement == None:
      raise Exception(f'{klass.__name__} has uninitialized measurement')

    if klass._fields == None:
      raise Exception(f'{klass.__name__} has uninitialized fields')

    if len(klass._fields) != len(properties):
      raise Exception(f'{klass.__name__} has mismatching properties and fields lengths')

    return {
      'measurement': klass._measurement,
      'fields': list(zip(klass._fields, properties)),
    }
