from .sensors.InfluxSensor import InfluxSensor

from .sensors.BME280     import BME280
from .sensors.FC37       import FC37
from .sensors.Anemometer import Anemometer
from .sensors.MPU6050    import MPU6050
from .sensors.MLX90614   import MLX90614
from .sensors.BH1750     import BH1750

KLASS_ID_MAPPING = {
  1: BME280,
  2: FC37,
  3: Anemometer,
  4: MPU6050,
  5: MLX90614,
  6: BH1750
}

def is_influx_sensor(klass):
  return issubclass(klass, InfluxSensor)
