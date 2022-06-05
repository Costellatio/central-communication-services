#include <SensorToggles.h>
#include <Timer.h>

Timer<> timer;

#ifdef BME280_ENABLED
  #include <BME280.h>

  BME280 _(timer);
#endif

void setup() {
  Serial.begin(9600);
}

void loop() {
  timer.tick();
}
