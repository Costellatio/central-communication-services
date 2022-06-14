from os        import getenv
from dotenv    import load_dotenv
from logging import INFO, info, warning, basicConfig
from websocket import create_connection
from json      import dumps

load_dotenv()
basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

CONTROL_PANEL_SOCKET_HOST = getenv('CONTROL_PANEL_SOCKET_HOST')

class ControlPanel:
  def __init__(self):
    self.socket = create_connection(CONTROL_PANEL_SOCKET_HOST)

  def process(self, klass, properties):
    sensor_data = klass().process(properties)
    self.socket.send(dumps({ 'y': properties[1] }))
    info(f'[{klass.__name__}] Data: {sensor_data}')
