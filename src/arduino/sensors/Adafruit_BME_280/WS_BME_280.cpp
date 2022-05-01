/**
 * @file WS_BME_280.cpp
 *
 * @brief Source file for weather station sensor.
 */

#include <Arduino.h>
#include "WS_BME_280.h"
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <SensorSerialDataBuilder.h>

#define SEALEVELPRESSURE_HPA            (1013.25)
#define WEATHER_STATION_MEASUREMENT     "weather station"
#define TEMPERATURE_FIELD               "temperature"
#define HUMIDITY_FIELD                  "humidity"
#define ATM_PRESSURE_FIELD              "atmospheric pressure"
#define ALTITUDE_FIELD                  "altitude"
#define DELAY_TIME                      5000    // Time in milliseconds

enum bme280_sensors {
  Temperature,
  Humidity,
  Pressure,
  Altitude,
  Sensors_Amount
};

String temperature_sensor_serial_data(Adafruit_BME280 &bme) {
  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(bme.readHumidity()));
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

void print_weather_station_data(Adafruit_BME280 bme)
{
  String serial_data;

  serial_data = "[" + temperature_sensor_serial_data(bme) + "," 
                    + humidity_sensor_serial_data(bme) + ","
                    + atm_pressure_sensor_serial_data(bme) + ","
                    + altitude_sensor_serial_data(bme) +
                "]";
  /*
  for(int i = 0; i < bme280_sensors::Sensors_Amount; i++)
  {
    switch(i) {
      case bme280_sensors::Temperature :
       
        break;

      case bme280_sensors::Humidity :
        serial_data = "[" + humidity_sensor_serial_data(bme) + "]";
        break;

      case bme280_sensors::Pressure :
        serial_data = "[" + atm_pressure_sensor_serial_data(bme) + "]";
        break;

      case bme280_sensors::Altitude :
        serial_data = "[" + altitude_sensor_serial_data(bme) + "]";
        break;

      default:
        break;
    }
*/
    Serial.println(serial_data);
//  }
  delay(5000);
}