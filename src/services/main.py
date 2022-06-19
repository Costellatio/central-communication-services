from env                  import Env
from logger               import Logger
from json                 import dumps
from serial_reader        import SerialReader
from influx_processor     import InfluxProcessor
from sensors.sensor_klass import SensorKlass
from flask                import Flask
from flask_socketio       import SocketIO

class App:
  @staticmethod
  def run():
    serial_reader = SerialReader()
    influx_processor = InfluxProcessor()

    flask_app = Flask(__name__)
    socket_connection = SocketIO(flask_app, cors_allowed_origins='*')

    def main_thread():
      while True:
        try:
          serial_data = serial_reader.read_one()

          id = serial_data[0]
          properties = serial_data[1:]
          klass = SensorKlass.get_klass(id)

          sensor_data = klass().process(properties)
          if SensorKlass.is_influx_sensor(klass):
            influx_processor.process(sensor_data)
          elif SensorKlass.is_control_sensor(klass):
            socket_connection.emit(klass.__name__, dumps(sensor_data))

          Logger.info(f'[{klass.__name__}] {sensor_data}')
        except KeyboardInterrupt:
          Logger.info('exiting...')
          exit(0)
        except Exception as error:
          Logger.warning(error)

    @socket_connection.event
    def connect():
      socket_connection.start_background_task(main_thread)

    socket_connection.run(flask_app, Env.get('SOCKET_HOST'), Env.get('SOCKET_PORT'))

if __name__ == '__main__':
  App.run()
