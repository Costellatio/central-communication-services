from .sensors.InfluxSensor       import InfluxSensor
from .sensors.ControlPanelSensor import ControlPanelSensor

from .sensors.BME280     import BME280
from .sensors.FC37       import FC37
from .sensors.Anemometer import Anemometer
from .sensors.MPU6050    import MPU6050

class SensorKlass:
  ID_MAP = {
    1: BME280,
    2: FC37,
    3: Anemometer,
    4: MPU6050,
  }

  @staticmethod
  def map_id(id):
    return SensorKlass.ID_MAP[id]

  @staticmethod
  def is_influx_type(klass):
    return issubclass(klass, InfluxSensor)

  @staticmethod
  def is_control_panel_type(klass):
    return issubclass(klass, ControlPanelSensor)
