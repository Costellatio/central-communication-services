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
  serial_connection.flush()

  while True:
    try:
      serial_data = loads(serial_connection.readline().decode())

      sensor_id = serial_data[0]
      sensor_properties = serial_data[1:]

      sensor = SENSOR_ID_MAPPING[sensor_id].process(sensor_properties)
      for (name, value) in sensor['field_data']:
        sensor_record = Point(sensor['measurement']).field(name, value)
        influx_write.write(bucket=influx_bucket, org=influx_org, record=sensor_record)

    except KeyboardInterrupt:
      info('service shutting down')
      exit(0)

    except Exception as error:
      warning(error)
      continue

run()
