from .logger import Logger

from json   import loads
from serial import Serial

class SerialPort(Serial):
  def __init__(self, port, rate):
    try:
      super(SerialPort, self).__init__(port, rate)

      self.reset_input_buffer()
      self.reset_output_buffer()
    except:
      Logger.warning(f'Serial Port {port} is busy or inactive')

  def read(self):
    return loads(self.readline().decode())
