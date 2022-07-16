import express from 'express';
import socketio from 'socket.io';
import http from 'http';
import dotenv from 'dotenv';

dotenv.config();

const app = express();
const server = http.createServer(app);
const socket = new socketio.Server(server);

socket.on('connection', (connection) => {
  console.log(`hekk hello ${connection}`);
});

server.listen(3030, () => {
  console.log('App listenings on port 3030');
});
