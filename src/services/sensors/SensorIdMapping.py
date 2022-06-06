from .BME280 import BME280
from .FC37 import FC37

SENSOR_ID_MAPPING = {
  1: BME280,
  2: FC37,
}
