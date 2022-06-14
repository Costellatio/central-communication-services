from os        import getenv
from dotenv    import load_dotenv
from json      import dumps
from websocket import create_connection

from .Logger import Logger

load_dotenv()

CONTROL_PANEL_HOST = getenv('CONTROL_PANEL_HOST')

class ControlPanel:
  def __init__(self):
    self.socket = create_connection(CONTROL_PANEL_HOST)

  def process(self, klass, properties):
    if self.socket.connected:
      data = klass().process(properties)
      self.socket.send(dumps(properties))

      Logger.info(f'[{klass.__name__}] Data: {data}')
    else:
      Logger.warning('control panel client is inactive\nforce shutting down')
      exit(1)
