from logging import INFO, getLogger, basicConfig

class Logger:
  _logger = None

  @staticmethod
  def init():
    if Logger._logger != None:
      return Logger._logger

    format = '[%(levelname)s][%(asctime)s] %(message)s'
    date_format = '%Y-%m-%d %H:%M:%S'

    Logger._logger = getLogger('Logger')
    basicConfig(level=INFO, format=format, datefmt=date_format)
    Logger._logger.setLevel(INFO)

  @staticmethod
  def info(message):
    Logger.init()
    Logger._logger.info(message)

  @staticmethod
  def warning(message):
    Logger.init()
    Logger._logger.info(message)
