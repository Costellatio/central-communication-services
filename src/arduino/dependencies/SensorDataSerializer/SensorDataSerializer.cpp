#include "SensorDataSerializer.h"
#include <Arduino.h>

#define MAX_SERIAL_DATA_SIZE 64
#define MAX_PIN_DATA_SIZE 2
#define MAX_PROPERTY_DATA_SIZE 10

#define INTEGER_BASE 10
#define MIN_FLOAT_WIDTH 1
#define FLOAT_PRECISION 2

const char* SensorDataSerializer::serialize(int pin, int properties_size, ...) {
  va_list properties;
  va_start(properties, properties_size);

  char serial_data[MAX_SERIAL_DATA_SIZE];

  strcat(serial_data, "[");
  strcat(serial_data, pin_data(pin));
  strcat(serial_data, ",");

  for (int i = 0; i < properties_size; i++) {
    float property = va_arg(properties, float);
    strcat(serial_data, property_data(property));

    if (i + 1 != properties_size) {
      strcat(serial_data, ",");
    }
  }

  strcat(serial_data, "]");

  va_end(properties);

  return serial_data;
}

const char* SensorDataSerializer::pin_data(int pin) {
  char pin_data[MAX_PIN_DATA_SIZE];
  itoa(pin, pin_data, INTEGER_BASE);
  return pin_data;
}

const char* SensorDataSerializer::property_data(float property) {
  char property_data[MAX_PROPERTY_DATA_SIZE];
  dtostrf(property, MIN_FLOAT_WIDTH, FLOAT_PRECISION, property_data);
  return property_data;
}
