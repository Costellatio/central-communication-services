#include "TMP_38GZ.h"
#include <SensorSerialDataBuilder.h>

#define TEMPERATURE_SENSOR_PIN      A0
#define WEATHER_STATION_MEASUREMENT "weather station"
#define TEMPERATURE_FIELD           "temperature"

String temperature_sensor_serial_data() {
  int    sensor_value   = analogRead(TEMPERATURE_SENSOR_PIN);
  float  sensor_voltage = (sensor_value / 1024.0) * 5.0;
  float  value          = (sensor_voltage - 0.5) * 100;

  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(value));
}
