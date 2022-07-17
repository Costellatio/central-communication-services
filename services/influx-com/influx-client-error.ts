import { ServiceError } from '../../utils/error';

class InfluxClientError extends ServiceError {
  constructor(message: string) {
    super('InfluxClientError', message);
  }
}

export default InfluxClientError;
