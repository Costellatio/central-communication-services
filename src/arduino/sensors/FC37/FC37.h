#ifndef FC37_H
#define FC37_H

#include <Sensor.h>

class FC37 : public Sensor {
public:
  FC37(Timer<>& timer);
  void run();
};

#endif
