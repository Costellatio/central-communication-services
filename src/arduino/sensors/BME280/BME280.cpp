#include "BME280.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

#define TICK_INTERVAL 2 * 1000UL
#define SEALEVELPRESSURE_HPA 1013.25
#define SERIALIZER_PROPERTIES 4

BME280::BME280(Timer<>& timer) : Sensor(timer) {}

void BME280::run() {
  bme.begin(BME280_I2C_ADDRESS);
  timer().every(TICK_INTERVAL, [](AdafruitBME280& bme) -> bool {
    float temperature = bme.readTemperature();
    float humidity = bme.readHumidity();
    float pressure = bme.readPressure() / 100.0F;
    float altitude = bme.readAltitude(SEALEVELPRESSURE_HPA);

    const char* data = SensorDataSerializer::serialize(BME280_ID, SERIALIZER_PROPERTIES, temperature, humidity, pressure, altitude);
    Serial.println(data);
    delete[] data;

    return true;
  }, &bme);
}
