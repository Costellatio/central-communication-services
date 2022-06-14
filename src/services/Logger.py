from logging import INFO, getLogger, basicConfig

class Logger:
  LOGGER = None

  @staticmethod
  def init_logger():
    if Logger.LOGGER != None:
      return Logger.LOGGER

    format = '[%(levelname)s][%(asctime)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    Logger.LOGGER = getLogger('Logger')
    basicConfig(level=INFO, format=format, datefmt=date_format)
    Logger.LOGGER.setLevel(INFO)

  @staticmethod
  def info(message):
    Logger.init_logger()
    Logger.LOGGER.info(message)

  @staticmethod
  def warning(message):
    Logger.init_logger()
    Logger.LOGGER.info(message)
