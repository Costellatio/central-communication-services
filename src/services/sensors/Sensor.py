class Sensor:
  MEASUREMENT = None
  FIELDS = None

  @staticmethod
  def process(properties):
    if __class__.__name__ == 'Sensor':
      raise Exception('Undefined behaviour. Class interface method `process` called')

    if __class__.MEASUREMENT == None:
      raise Exception('Uninitialized measurement constant')

    if __class__.FIELDS == None:
      raise Exception('Uninitialized fields constant')

    if len(__class__.FIELDS) != len(properties):
      raise Exception('Mismatching properties and fields lengths')

    return {
      'measurement': __class__.MEASUREMENT,
      'field_data': __class__.FIELDS.zip(properties)
    }
