from .influx_sensor  import InfluxSensor
from .control_sensor import ControlSensor

from .bme280     import BME280
from .fc37       import FC37
from .anemometer import Anemometer
from .mpu6050    import MPU6050

class SensorKlass:
  _sensor_id_dictionary = {
    1: BME280,
    2: FC37,
    3: Anemometer,
    4: MPU6050,
  }

  @staticmethod
  def get_klass(id):
    return SensorKlass._sensor_id_dictionary[id]

  @staticmethod
  def is_influx_sensor(klass):
    return issubclass(klass, InfluxSensor)

  @staticmethod
  def is_control_sensor(klass):
    return issubclass(klass, ControlSensor)
