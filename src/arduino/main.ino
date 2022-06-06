#include <SensorToggles.h>
#include <Timer.h>
#include <WS_Rain_Sensor.h>

Timer<> timer;

#ifdef BME280_ENABLED
  #include <BME280.h>

  BME280 bme280(timer);
#endif

#ifdef FC37_ENABLED
  #include <FC37.h>

  FC37 fc37(timer);
#endif

void setup() {
  Serial.begin(9600);

  #ifdef BME280_ENABLED
    bme280.run();
  #endif

  #ifdef FC37_ENABLED
    fc37.run();
  #endif
}

void loop() {
  timer.tick();
}
