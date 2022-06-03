/**
 * @file WS_BME_280.cpp
 *
 * @brief Header file for weather station sensor.
 */

#ifndef _WS_BME_280
#define _WS_BME_280
#include <Adafruit_BME280.h>

void assemble_data(char* buffer, Adafruit_BME280& bme);
bool print_weather_station_data(Adafruit_BME280 bme);

#endif  // _WS_BME_280