#ifndef SENSOR_H
#define SENSOR_H

#include <Timer.h>

class Sensor {
protected:
  Timer<> _timer;

public:
  Sensor(Timer<>& timer);
};

#endif
