from os              import getenv
from serial          import Serial
from dotenv          import load_dotenv
from influxdb_client import InfluxDBClient, Point
from logging         import INFO, info, warning, basicConfig

basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')
load_dotenv()

influx_url    = getenv('INFLUXDB_HOST')
influx_bucket = getenv('INFLUXDB_BUCKET')
influx_org    = getenv('INFLUXDB_ORG')
influx_token  = getenv('INFLUXDB_TOKEN')

arduino_port = getenv('ARDUINO_PORT')
arduino_rate = getenv('ARDUINO_RATE')

def switch_get_filter(argument):
  switcher = {
    1: "weather station",
    10: "temperature",
    11: "humidity",
    12: "atmospheric pressure",
    13: "altitude",
    14: "wind speed"
  }
  return switcher.get(argument, "INVALID ARGUMENT")

def send_data(data):
  data = data.split(",")
  if len(data) != 2:
    raise Exception("Expected 2 arguments from serial data, recieved: " + str(len(data)))

  _measurement = int((data[0])[0])

  if data[0] == "INVALID ARGUMENT":
    raise Exception("Sensor ID is unknown!")
  _field = int(data[0])
  _data = float(data[1])

  influx_point = Point(switch_get_filter(_measurement)).field(switch_get_filter(_field), _data)
  influx_write.write(bucket=influx_bucket, org=influx_org, record=influx_point)

  info('data written')

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
      serial_data = serial_connection.readline().decode().strip()
      serial_data = serial_data.replace(" ", "")
      serial_data = serial_data.split("#")

      for data in serial_data:
        if data:
          send_data(data)

    except KeyboardInterrupt:
      info('service shutting down')
      exit(0)
    except Exception as e:
      warning(e)
      warning('broken data')
      continue

run()
