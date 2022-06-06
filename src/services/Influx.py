from os                      import getenv
from serial                  import Serial
from dotenv                  import load_dotenv
from influxdb_client         import InfluxDBClient, Point
from logging                 import INFO, info, warning, basicConfig
from json                    import loads
from sensors.SensorIdMapping import SENSOR_ID_MAPPING

basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')
load_dotenv()

influx_url    = getenv('INFLUXDB_HOST')
influx_bucket = getenv('INFLUXDB_BUCKET')
influx_org    = getenv('INFLUXDB_ORG')
influx_token  = getenv('INFLUXDB_TOKEN')

arduino_port = getenv('ARDUINO_PORT')
arduino_rate = getenv('ARDUINO_RATE')

try:
  influx_client = InfluxDBClient(url=influx_url, org=influx_org, token=influx_token)
  influx_write  = influx_client.write_api()
except:
  info('not able to connect to influx')
  exit(1)

try:
  serial_connection = Serial(arduino_port, arduino_rate)
except:
  info('not able to connect to arduino serial port')
  exit(1)

def run():
  info('service listening for serial data')
  serial_connection.reset_input_buffer()
  serial_connection.reset_output_buffer()

  while True:
    try:
      serial_data = loads(serial_connection.readline().decode())

      sensor_id = serial_data[0]
      sensor_properties = serial_data[1:]
      sensor_class = SENSOR_ID_MAPPING[sensor_id]

      sensor_data = sensor_class().process(sensor_properties)
      for (name, value) in sensor_data['fields']:
        sensor_record = Point(sensor_data['measurement']).field(name, value)
        influx_write.write(bucket=influx_bucket, org=influx_org, record=sensor_record)

      info(f'[{sensor_class.__name__}] Measurement: {sensor_data["measurement"]}, Fields: {sensor_data["fields"]}')
    except KeyboardInterrupt:
      info('service shutting down')
      exit(0)
    except Exception as error:
      warning(error)
      continue

run()
