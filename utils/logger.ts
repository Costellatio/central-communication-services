import { createLogger, transports, format } from 'winston';

const logger = createLogger({
  level: 'info',
  transports: [
    new transports.Console(),
  ],
});

const loggerFormat = format.printf(({ level, message, label, timestamp }) => {
  return `${timestamp} [${label}] ${level}: ${message}`;
});

function logInfo(label: string, message: string) {
  logger.configure({
    format: format.combine(
      format.label({ label }),
      format.timestamp(),
      loggerFormat,
    ),
  });

  logger.log('info', message);
}

function logError(label: string, message: string) {
  logger.configure({
    format: format.combine(
      format.label({ label }),
      format.timestamp(),
      loggerFormat,
    ),
  });

  logger.log('error', message);
}

export {
  logInfo,
  logError,
};
