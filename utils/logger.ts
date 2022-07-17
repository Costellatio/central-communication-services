import { createLogger, transports, format } from 'winston';

const loggerFormat = format.printf(({ level, message, label, timestamp }) => {
  return `[${level.toUpperCase()}][${label}][${timestamp}]: ${message}`;
});

const getLogger = (label: string) => createLogger({
  level: 'info',
  transports: [
    new transports.Console(),
    new transports.File({ filename: 'logs/prod.log' }),
  ],
  format: format.combine(
    format.label({ label }),
    format.timestamp({ format: 'MMM-DD-YYYY HH:mm:ss' }),
    loggerFormat,
  ),
});

function logInfo(label: string, message: string) {
  getLogger(label).log('info', message);
}

function logError(label: string, message: string) {
  getLogger(label).log('error', message);
}

export {
  logInfo,
  logError,
};
