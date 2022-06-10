from os      import getenv
from dotenv  import load_dotenv
from logging import INFO, info, warning, basicConfig
from json    import loads
from serial  import Serial

from .Influx         import Influx
from .KlassIdMapping import KLASS_ID_MAPPING, is_influx_sensor

load_dotenv()
basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

serial_port = getenv('SERIAL_PORT')
serial_rate = getenv('SERIAL_RATE')

try:
  serial = Serial(serial_port, serial_rate)
except:
  warning('serial communication is inactive\nshutting down')
  exit(1)

class SerialProcessor:
  @staticmethod
  def listen():
    info('serial processor listening')
    serial.reset_input_buffer()
    serial.reset_output_buffer()

    while True:
      try:
        serial_data = loads(serial.readline().decode())
      except KeyboardInterrupt:
        info('shutting down')
        exit(0)
      except Exception as error:
        warning(error)
        continue

      id = serial_data[0]
      properties = serial_data[1:]
      klass = KLASS_ID_MAPPING[id]

      if is_influx_sensor(klass):
        Influx.process(klass, properties)
      else:
        info(f'[{klass.__name__}] Data: {klass().process(properties)}')

SerialProcessor.listen()
