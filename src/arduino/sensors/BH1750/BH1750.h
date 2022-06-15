#ifndef BH_1750_H
#define BH_1750_H

#include <Sensor.h>
#include <BH1750.h>

class BH1750 : public Sensor {
private:
  BH1750 lightMeter;

public:
  BH1750(Timer<>& timer);
  void run();
};

#endif
