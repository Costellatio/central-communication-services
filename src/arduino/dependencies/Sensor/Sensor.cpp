#include "Sensor.h"

Sensor::Sensor(Timer<>& timer) : _timer(timer) {}

Timer<>& Sensor::timer() {
  return _timer;
}
