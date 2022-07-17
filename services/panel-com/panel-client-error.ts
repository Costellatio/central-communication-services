import { ServiceError } from '../../utils/error';

class PanelClientError extends ServiceError {
  constructor(message: string) {
    super('PanelClientError', message);
  }
}

export default PanelClientError;
