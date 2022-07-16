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

import { ArduinoSerial } from 'services/arduino-station-com';

dotenv.config();

const arduinoSerial = new ArduinoSerial();

arduinoSerial.open();

arduinoSerial.on('data', (data) => {
  console.log(data);
});
