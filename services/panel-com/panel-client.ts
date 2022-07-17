import express from 'express';
import http from 'http';
import socketio from 'socket.io';
import PanelClientError from './panel-client-error';
import { logInfo } from '../../utils/logger';

class PanelClient {
  app: express.Express;
  server: http.Server;
  socket: socketio.Server;

  constructor() {
    if (process.env.CONTROL_PANEL_PORT === undefined) {
      throw new PanelClientError('CONTROL_PANEL_PORT environment variable not specified');
    }

    this.app = express();
    this.server = http.createServer(this.app);
    this.socket = new socketio.Server(this.server);

    this.server.listen(process.env.CONTROL_PANEL_PORT, () => {
      logInfo('PanelClient', `Socket opened on port ${process.env.CONTROL_PANEL_PORT}`);
    });
  }

  emit(name: string, message: any) {
    this.socket.emit(name, message);
  }
}

export default PanelClient;
