import { SerialPort } from 'serialport';
import { logInfo, logError } from 'utils/logger';

const DEFAULT_SERIAL_PORT = '/dev/ttyACM0';
const DEFAULT_BAUD_RATE = 9600;

class ArduinoSerial extends SerialPort {
  constructor() {
    super({
      path: process.env.ARDUINO_SERIAL_PORT || DEFAULT_SERIAL_PORT,
      baudRate: Number(process.env.ARDUINO_BAUD_RATE) || DEFAULT_BAUD_RATE,
      autoOpen: false,
    });
  }

  open() {
    super.open((error) => {
      if (error) {
        logError('ArduinoSerial', error.message);
      }

      logInfo('ArduinoSerial', `Successfully connected to serial port ${this.path}`);
    });
  }
}

export default ArduinoSerial;
