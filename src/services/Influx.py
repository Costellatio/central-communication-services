from os              import getenv
from dotenv          import load_dotenv
from logging         import INFO, info, basicConfig, warning
from influxdb_client import InfluxDBClient, Point

load_dotenv()
basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

INFLUX_URL    = getenv('INFLUXDB_HOST')
INFLUX_BUCKET = getenv('INFLUXDB_BUCKET')
INFLUX_ORG    = getenv('INFLUXDB_ORG')
INFLUX_TOKEN  = getenv('INFLUXDB_TOKEN')

class Influx:
  def __init__(self):
    self.client = InfluxDBClient(url=INFLUX_URL, org=INFLUX_ORG, token=INFLUX_TOKEN)
    self.write_api = self.client.write_api()

  def process(self, klass, properties):
    if self.client.ping():
      sensor_data = klass().process(properties)
      for (name, value) in sensor_data['fields']:
        sensor_record = Point(sensor_data['measurement']).field(name, value)
        self.write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=sensor_record)

      info(f'[{klass.__name__}] Measurement: {sensor_data["measurement"]}, Fields: {sensor_data["fields"]}')
    else:
      warning('influx client is inactive\nshutting down')
      exit(1)
