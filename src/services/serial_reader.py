from env    import Env
from logger import Logger
from json   import loads
from serial import Serial

class SerialReader(Serial):
  def __init__(self):
    try:
      super(SerialReader, self).__init__(Env.get('SERIAL_PORT'), Env.get('SERIAL_RATE'))

      self.reset_input_buffer()
      self.reset_output_buffer()
    except Exception as e:
      Logger.warning(e)
      Logger.warning('serial communication is inactive - exiting...')
      exit(1)

  def read_one(self):
    return loads(self.readline().decode())
