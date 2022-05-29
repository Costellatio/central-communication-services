#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <SensorSerialDataBuilder.h>

#define SEALEVELPRESSURE_HPA        (1013.25)
#define WEATHER_STATION_MEASUREMENT "weather station"
#define TEMPERATURE_FIELD           "temperature"

Adafruit_BME280 bme;

/*
bme.readTemperature()
bme.readPressure() / 100.0F
bme.readAltitude(SEALEVELPRESSURE_HPA)
bme.readHumidity()
*/

String temperature_sensor_serial_data() {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(bme.readTemperature()));
}

void setup() {
  Serial.begin(9600);

  if (!bme.begin(0x76)) {
    Serial.println("No BME280 device found!");
    while (1);
  }
}

void loop() {
  String serial_data = "[" +
    temperature_sensor_serial_data() +
  "]";

  Serial.println(serial_data);
  delay(2000);
}
