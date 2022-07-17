import { ServiceError } from '../../utils/error';

class ArduinoSerialError extends ServiceError {
  constructor(message: string) {
    super('ArduinoSerialError', message);
  }
}

export default ArduinoSerialError;
