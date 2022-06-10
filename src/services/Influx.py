from os              import getenv
from dotenv          import load_dotenv
from logging         import INFO, info, basicConfig, warning
from influxdb_client import InfluxDBClient, Point

load_dotenv()
basicConfig(level=INFO, format='[%(levelname)s][%(asctime)s] %(message)s')

influx_url    = getenv('INFLUXDB_HOST')
influx_bucket = getenv('INFLUXDB_BUCKET')
influx_org    = getenv('INFLUXDB_ORG')
influx_token  = getenv('INFLUXDB_TOKEN')

influx_client = InfluxDBClient(url=influx_url, org=influx_org, token=influx_token)
influx_write  = influx_client.write_api()

class Influx:
  @staticmethod
  def process(sensor_klass, properties):
    if influx_client.ping():
      sensor_data = sensor_klass().process(properties)
      for (name, value) in sensor_data['fields']:
        sensor_record = Point(sensor_data['measurement']).field(name, value)
        influx_write.write(bucket=influx_bucket, org=influx_org, record=sensor_record)

      info(f'[{sensor_klass.__name__}] Measurement: {sensor_data["measurement"]}, Fields: {sensor_data["fields"]}')
    else:
      warning('influx client is inactive\nshutting down')
      exit(1)
