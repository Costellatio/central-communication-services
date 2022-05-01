#ifndef _WS_BME_280
#define _WS_BME_280
#include <Adafruit_BME280.h>

/**
 * @file WS_BME_280.cpp
 *
 * @brief Header file for weather station sensor.
 */

String temperature_sensor_serial_data(Adafruit_BME280 &bme);
String humidity_sensor_serial_data(Adafruit_BME280 &bme);
String atm_pressure_sensor_serial_data(Adafruit_BME280 &bme);
String altitude_sensor_serial_data(Adafruit_BME280 &bme);

void print_weather_station_data(Adafruit_BME280 bme);

#endif  // _WS_BME_280