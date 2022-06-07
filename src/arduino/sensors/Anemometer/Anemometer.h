#ifndef ANEMOMETER_H
#define ANEMOMETER_H

#include <Sensor.h>

class Anemometer : public Sensor {
public:
  Anemometer(Timer<>& timer);
  void run();
};

#endif
