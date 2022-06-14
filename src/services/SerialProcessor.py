from os      import getenv
from dotenv  import load_dotenv
from logging import INFO, info, warning, basicConfig
from json    import loads
from serial  import Serial

from .SensorKlass  import SensorKlass
from .Influx       import Influx
from .ControlPanel import ControlPanel

load_dotenv()
basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

SERIAL_PORT = getenv('SERIAL_PORT')
SERIAL_RATE = getenv('SERIAL_RATE')

class SerialProcessor:
  def __init__(self):
    try:
      self.serial = Serial(SERIAL_PORT, SERIAL_RATE)
    except:
      warning('serial communication is inactive\nshutting down')
      exit(1)

  def listen(self):
    info('serial processor listening')

    influx = Influx()
    control_panel = ControlPanel()

    self.serial.reset_input_buffer()
    self.serial.reset_output_buffer()

    while True:
      try:
        serial_data = loads(self.serial.readline().decode())
      except KeyboardInterrupt:
        info('shutting down')
        exit(0)
      except Exception as error:
        warning(error)
        continue

      id = serial_data[0]
      properties = serial_data[1:]
      klass = SensorKlass.map_id(id)

      if SensorKlass.is_influx_type(klass):
        influx.process(klass, properties)
      elif SensorKlass.is_control_panel_type(klass):
        control_panel.process(klass, properties)
