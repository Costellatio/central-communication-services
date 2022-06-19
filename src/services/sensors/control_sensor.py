from .sensor import Sensor

class ControlSensor(Sensor):
  def process(self, properties):
    return {
      'data': properties
    }
