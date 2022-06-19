from .bme280     import BME280
from .fc37       import FC37
from .anemometer import Anemometer

class Sensor:
  _measurement = None
  _fields = None

  _class_dictionary = {
    1: BME280,
    2: FC37,
    3: Anemometer,
  }

  @classmethod
  def process(klass, properties):
    if klass._measurement == None:
      raise Exception(f'{klass.__name__} has uninitialized measurement')

    if klass._fields == None:
      raise Exception(f'{klass.__name__} has uninitialized fields')

    if len(klass._fields) == len(properties):
      raise Exception(f'{klass.__name__} has mismatching properties and fields lengths')

    return {
      'measurement': klass._measurement,
      'fields': list(zip(klass._fields, properties))
    }

  @staticmethod
  def get_sensor_class(sensor_id):
    return Sensor._class_dictionary[sensor_id]
