from abc import ABC, abstractmethod

class Sensor(ABC):
  @abstractmethod
  def process(self, properties):
    pass
