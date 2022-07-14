from .logger import Logger

from json   import loads
from serial import Serial

class SerialPort(Serial):
  def __init__(self, port, rate):
    try:
      super(SerialPort, self).__init__(port, rate)
    except:
      Logger.warning(f'Serial Port {port} is busy or inactive')
      exit(1)

    self.reset_input_buffer()
    self.reset_output_buffer()

  def read_data(self):
    return loads(self.readline().decode())
