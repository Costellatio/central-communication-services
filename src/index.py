from os import getenv
from serial import Serial
from dotenv import load_dotenv
from influxdb_client import InfluxDBClient, Point
from json import loads

# Setup
load_dotenv()

influx_url = getenv('INFLUXDB_HOST')
bucket     = getenv('INFLUXDB_BUCKET')
org        = getenv('INFLUXDB_ORG')
token      = getenv('INFLUXDB_TOKEN')

try:
  influx_client = InfluxDBClient(url = influx_url, org = org, token = token)
  influx_write  = influx_client.write_api()
  influx_read   = influx_client.query_api()
except:
  print('fatal: Make sure InfluxDB is running and admin credentials are correct!')
  exit(1)

try:
  serial_connection = Serial(getenv('ARDUINO_PORT'), getenv('ARDUINO_RATE'))
except:
  print('fatal: Make sure your Arduino is connected and the environment port is correct!')
  exit(1)

# Actions
def listen():
  print('Listening for arduino signals!\n')

  serial_connection.flush()

  while True:
    try:
      serial_data = loads(serial_connection.readline().decode().strip())

      for data in serial_data:
        sensor_record = Point(data['measurement']).field(data['field'], data['value'])
        influx_write.write(bucket = bucket, org = org, record = sensor_record)

      print('info: Data Written...')
    except KeyboardInterrupt:
      print('Ending process...')
      exit(0)
    except:
      print('fatal: Internal Error!')
      continue

# Run
listen()
