from os              import getenv
from dotenv          import load_dotenv
from influxdb_client import InfluxDBClient, Point

from .Logger import Logger

load_dotenv()

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
      data = klass().process(properties)
      for (name, value) in data['fields']:
        record = Point(data['measurement']).field(name, value)
        self.write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=record)

      Logger.info(f'[{klass.__name__}] Measurement: {data["measurement"]}, Fields: {data["fields"]}')
    else:
      Logger.warning('influx client is inactive\nforce shutting down')
      exit(1)
