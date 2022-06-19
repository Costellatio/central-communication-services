from .bme280     import BME280
from .fc37       import FC37
from .anemometer import Anemometer

class SensorClassMapper:
  _class_dictionary = {
    1: BME280,
    2: FC37,
    3: Anemometer,
  }

  @staticmethod
  def map(sensor_id):
    return SensorClassMapper._class_dictionary[sensor_id]
