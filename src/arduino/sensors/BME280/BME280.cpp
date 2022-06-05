#include "BME280.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorPins.h>

#define TICK_INTERVAL 2 * 1000UL
#define SEALEVELPRESSURE_HPA 1013.25
#define SERIALIZER_PROPERTIES 4

BME280::BME280(Timer<>& timer) : Sensor(timer) {
  bme.begin(BME280_PIN);
  timer.every(TICK_INTERVAL, [](AdafruitBME280& bme) -> bool {
    float temperature = bme.readTemperature();
    float humidity = bme.readHumidity();
    float pressure = bme.readPressure() / 100.0F;
    float altitude = bme.readAltitude(SEALEVELPRESSURE_HPA);

    Serial.println(SensorDataSerializer::serialize(BME280_ID, SERIALIZER_PROPERTIES, temperature, humidity, pressure, altitude));

    return true;
  }, &bme);
}
