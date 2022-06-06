#ifndef SENSOR_H
#define SENSOR_H

#include <Timer.h>

class Sensor {
private:
  Timer<>& _timer;

protected:
  Timer<>& timer();

public:
  Sensor(Timer<>& timer);
  virtual void run() = 0;
};

#endif
