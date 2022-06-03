/**
 * @file WS_BME_280.cpp
 *
 * @brief Source file for weather station sensor.
 */

#include <Arduino.h>
#include "WS_BME_280.h"
#include <Wire.h>
#include <SensorSerialDataBuilder.h>
#include <common.h>

void assemble_data(char* buffer, Adafruit_BME280& bme)
{
  char *temperature = send_data_double(WS_TEMPERATURE, bme.readTemperature());
  char *humidity = send_data_double(WS_HUMIDITY, bme.readHumidity());
  char *atm_pressure = send_data_double(WS_ATM_PRESSURE, bme.readPressure() / 100.0F);
  char *altitute = send_data_double(WS_ALTITUDE, bme.readAltitude(SEALEVELPRESSURE_HPA));

  strcat(buffer, "#");
  strcpy(buffer, temperature);
  strcat(buffer, "#");
  strcat(buffer, humidity);
  strcat(buffer, "#");
  strcat(buffer, atm_pressure);
  strcat(buffer, "#");
  strcat(buffer, altitute);
  // if you want to add more sensors use strcat()
  
  strcat(buffer, "#");


  delete[] temperature;
  delete[] humidity;
  delete[] atm_pressure;
  delete[] altitute;
}

bool print_weather_station_data(Adafruit_BME280 bme)
{
  char serial_data[MAX_SIZE_WS_DATA_STORAGE];
  assemble_data(serial_data, bme);
  Serial.println(serial_data);
  return true;
}