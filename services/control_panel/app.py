from ..common.env         import Env
from ..common.logger      import Logger
from ..common.serial_port import SerialPort

from json           import dumps
from threading      import Lock
from flask          import Flask
from flask_socketio import SocketIO

process_thread = None
process_thread_lock = Lock()

flask_app = Flask(__name__)
socket = SocketIO(flask_app, cors_allowed_origins='*')
serial_port = SerialPort(Env.get('CP_SERIAL_PORT'), Env.get('CP_SERIAL_RATE'))

def main_process():
  while True:
    try:
      serial_data = serial_port.read_data()
      sensor_data = serial_data[1:]

      socket.emit('sensor_data', dumps({ 'data': sensor_data }))
      Logger.info(f'Sensor Data: {sensor_data}')
    except Exception as exception:
      Logger.warning(exception)

@socket.event
def connect():
  global process_thread
  with process_thread_lock:
    if process_thread == None:
      process_thread = socket.start_background_task(main_process)

if __name__ == '__main__':
  socket.run(flask_app, Env.get('CP_SOCKET_HOST'), Env.get('CP_SOCKET_PORT'))
