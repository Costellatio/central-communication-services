/**
 * @file WS_BME_280.cpp
 *
 * @brief Source file for weather station sensor.
 */

#include <Arduino.h>
#include "WS_BME_280.h"
#include <Wire.h>
#include <SensorSerialDataBuilder.h>

#define SEALEVELPRESSURE_HPA            (1013.25)
#define WEATHER_STATION_MEASUREMENT     "weather station"
#define TEMPERATURE_FIELD               "temperature"
#define HUMIDITY_FIELD                  "humidity"
#define ATM_PRESSURE_FIELD              "atmospheric pressure"
#define ALTITUDE_FIELD                  "altitude"

String temperature_sensor_serial_data(Adafruit_BME280 &bme) {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(bme.readTemperature()));
}
String humidity_sensor_serial_data(Adafruit_BME280 &bme) {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, HUMIDITY_FIELD, String(bme.readHumidity()));
}
String atm_pressure_sensor_serial_data(Adafruit_BME280 &bme) {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, ATM_PRESSURE_FIELD, String(bme.readPressure() / 100.0F));
}
String altitude_sensor_serial_data(Adafruit_BME280 &bme) {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, ALTITUDE_FIELD, String(bme.readAltitude(SEALEVELPRESSURE_HPA)));
}

bool print_weather_station_data(Adafruit_BME280 bme)
{
  String serial_data;

  serial_data = "[" + temperature_sensor_serial_data(bme) + "," 
                    + humidity_sensor_serial_data(bme) +
                "]";
  Serial.println(serial_data);
  return true;
}