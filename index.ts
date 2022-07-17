import dotenv from 'dotenv';

import { ArduinoSerial, ArduinoSerialError, Sensor } from './services/arduino-station-com';
import { InfluxClient, InfluxClientError } from './services/influx-com';
import { PanelClient, PanelClientError } from './services/panel-com';
import { logError, logInfo } from './utils/logger';

dotenv.config();

const arduinoSerial = new ArduinoSerial();
const influxClient  = new InfluxClient();
const panelClient   = new PanelClient();

arduinoSerial.open((data) => {
  try {
    const [sensorId, ...sensorProperties] = JSON.parse(data);
    const sensor = new Sensor(sensorId, sensorProperties);

    if (sensor.influxProps) {
      influxClient.write(sensor);
    }

    panelClient.emit(sensor.name, sensor.props);

    logInfo('Main', JSON.stringify(sensor.props));
  } catch (error: any) {
    if (
      error instanceof ArduinoSerialError ||
      error instanceof InfluxClientError  ||
      error instanceof PanelClientError
    ) {
      logError(error.name, error.message);
    } else {
      logError('UnknownError', error.message);
    }
  }
});
