from os              import getenv
from serial          import Serial
from dotenv          import load_dotenv
from influxdb_client import InfluxDBClient, Point
from json            import loads
from logging         import INFO, info, warning, basicConfig
import grafana

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
      for data in serial_data:
        sensor_record = Point(data['measurement']).field(data['field'], data['value'])

        for tag in data['tags']:
          sensor_record = sensor_record.tag(tag['name'], tag['value'])

        influx_write.write(bucket=influx_bucket, org=influx_org, record=sensor_record)

      info('data written')
    except KeyboardInterrupt:
      info('service shutting down')
      exit(0)
    except:
      warning('broken data')
      continue

run()
