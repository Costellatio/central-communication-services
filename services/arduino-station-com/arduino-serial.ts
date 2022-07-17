import { SerialPort, ReadlineParser } from 'serialport';
import { logInfo, logError } from '../../utils/logger';
import ArduinoSerialError from './arduino-serial-error';

class ArduinoSerial extends SerialPort {
  constructor() {
    if (process.env.ARDUINO_SERIAL_PORT === undefined) {
      throw new ArduinoSerialError('ARDUINO_SERIAL_PORT environment variable not specified');
    }

    if (process.env.ARDUINO_BAUD_RATE === undefined) {
      throw new ArduinoSerialError('ARDUINO_BAUD_RATE environment variable not specified');
    }

    super({
      path: process.env.ARDUINO_SERIAL_PORT,
      baudRate: Number(process.env.ARDUINO_BAUD_RATE),
      autoOpen: false,
    });
  }

  open(listener: (data: any) => void) {
    super.open((error) => {
      if (error) {
        logError('ArduinoSerial', `Serial port ${this.path} not found`);
        return;
      }

      logInfo('ArduinoSerial', `Successfully connected to serial port ${this.path}`);
    });

    const parser = new ReadlineParser();
    this.pipe(parser);
    parser.on('data', listener);
  }
}

export default ArduinoSerial;
