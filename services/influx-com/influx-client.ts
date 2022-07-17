import { InfluxDB, Point, WriteApi } from '@influxdata/influxdb-client';
import InfluxClientError from './influx-client-error';
import { Sensor } from '../arduino-station-com';

class InfluxClient extends InfluxDB {
  private writeApi: WriteApi;

  constructor() {
    if (process.env.INFLUX_URL === undefined) {
      throw new InfluxClientError('INFLUX_URL environment variable not specified');
    }

    if (process.env.INFLUX_TOKEN === undefined) {
      throw new InfluxClientError('INFLUX_TOKEN environment variable not specified');
    }

    if (process.env.INFLUX_ORG === undefined) {
      throw new InfluxClientError('INFLUX_ORG environment variable not specified');
    }

    if (process.env.INFLUX_BUCKET === undefined) {
      throw new InfluxClientError('INFLUX_BUCKET environment variable not specified');
    }

    super({
      url: process.env.INFLUX_URL,
      token: process.env.INFLUX_TOKEN,
    });

    this.writeApi = this.getWriteApi(process.env.INFLUX_ORG, process.env.INFLUX_BUCKET);
  }

  write(sensor: Sensor) {
    Object.entries(sensor.props).forEach(([field, value]) => {
      this.writeApi.writePoint(new Point(sensor.influxProps?.measurement).floatField(field, value));
    });
  }
}

export default InfluxClient;
