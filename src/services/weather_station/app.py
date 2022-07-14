from ..common.env         import Env
from ..common.logger      import Logger
from ..common.serial_port import SerialPort

from .influx_processor            import InfluxProcessor
from .sensors.sensor_class_mapper import SensorClassMapper

serial_port = SerialPort(Env.get('WS_SERIAL_PORT'), Env.get('WS_SERIAL_RATE'))
influx_processor = InfluxProcessor()

if __name__ == '__main__':
  try:
    Logger.info('/=== Weather Station ===/')
    while True:
      try:
        serial_data = serial_port.read_data()

        sensor_id = serial_data[0]
        sensor_properties = serial_data[1:]
        sensor_class = SensorClassMapper.map(sensor_id)
        sensor_data = sensor_class.process(sensor_properties)

        influx_processor.process(sensor_data)
        Logger.info(f'[{sensor_class.__name__}] {sensor_data}')
      except Exception as exception:
        Logger.warning(exception)
  except KeyboardInterrupt:
    Logger.info('/=== Exiting... ===/')
