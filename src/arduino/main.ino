#include <SensorToggles.h>
#include <Timer.h>

Timer<> timer;

#ifdef BME280_ENABLED
  #include <BME280.h>

  BME280 bme280(timer);
#endif

void setup() {
  Serial.begin(9600);

  #ifdef BME280_ENABLED
    bme280.run();
  #endif
}

void loop() {
  timer.tick();
}
