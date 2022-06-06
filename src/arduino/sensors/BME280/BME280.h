#ifndef BME_280_H
#define BME_280_H

#include <Sensor.h>
#include <AdafruitBME280.h>

class BME280 : public Sensor {
private:
  AdafruitBME280 bme;

public:
  BME280(Timer<>& timer);
  void run();
};

#endif
