from ..common.env    import Env
from ..common.logger import Logger

from influxdb_client import InfluxDBClient, Point

class InfluxProcessor(InfluxDBClient):
  def __init__(self):
    super(InfluxProcessor, self).__init__(
      url = Env.get('INFLUXDB_HOST'),
      org = Env.get('INFLUXDB_ORG'),
      token = Env.get('INFLUXDB_TOKEN'),
    )
    self._write_api = self.write_api()

  def process(self, data):
    if self.ping():
      for (name, value) in data['fields']:
        record = Point(data['measurement']).field(name, value)
        self._write_api.write(
          bucket = Env.get('INFLUXDB_BUCKET'),
          org = Env.get('INFLUXDB_ORG'),
          record = record,
        )
    else:
      Logger.warning('Influx client is inactive')
      exit(1)
