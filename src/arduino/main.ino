#include <SensorToggles.h>
#include <Timer.h>
#include <Wire.h>

Timer<> timer;

#ifdef BME280_ENABLED
  #include <BME280.h>

  BME280 bme280(timer);
#endif

#ifdef FC37_ENABLED
  #include <FC37.h>

  FC37 fc37(timer);
#endif

#ifdef ANEMOMETER_ENABLED
  #include <Anemometer.h>

  Anemometer anemometer(timer);
#endif

#ifdef MPU6050_ENABLED
  #include <MPU6050.h>

  MPU6050 mpu6050(timer);
#endif

#ifdef MLX90614_ENABLED
  #include <Adafruit_MLX90614.h>

  MLX90614 mlx90614(timer);
#endif

#ifdef BH1750_ENABLED
  #include <BH1750.h>

  BH1750 bh1750(timer);
#endif

void setup() {
  Serial.begin(9600);
  Wire.begin();

  #ifdef BME280_ENABLED
    bme280.run();
  #endif

  #ifdef FC37_ENABLED
    fc37.run();
  #endif

  #ifdef ANEMOMETER_ENABLED
    anemometer.run();
  #endif

  #ifdef MPU6050_ENABLED
    mpu6050.run();
  #endif

  #ifdef MLX90614_ENABLED
    mlx90614.run();
  #endif

  #ifdef BH1750_ENABLED
    bh1750.run();
  #endif
}

void loop() {
  timer.tick();
}
