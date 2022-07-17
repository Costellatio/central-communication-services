// import express from 'express';
// import socketio from 'socket.io';
// import http from 'http';

// const app = express();
// const server = http.createServer(app);
// const socket = new socketio.Server(server);

// server.listen(3030, () => {
//   console.log('App listenings on port 3030');
// });

import dotenv from 'dotenv';

import { ArduinoSerial, Sensor } from './services/arduino-station-com';
import { InfluxClient } from './services/influx-com';

dotenv.config();

const arduinoSerial = new ArduinoSerial();
const influxClient = new InfluxClient();

arduinoSerial.open((data) => {
  const [sensorId, ...sensorProperties] = JSON.parse(data);
  const sensor = new Sensor(sensorId, sensorProperties);

  if (sensor.influxProps) {
    influxClient.write(sensor);
  }

  // controlPanel.emit(sensor.name, sensor.props)

  console.log(data);
});
