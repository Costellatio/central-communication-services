#ifndef MPU6050_H
#define MPU6050_H

#include <Sensor.h>

class MPU6050 : public Sensor {
public:
  MPU6050(Timer<>& timer);
  void run();
};

#endif
