#include "Anemometer.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

#define TICK_INTERVAL 2 * 1000UL
#define SERIALIZER_PROPERTIES 1

Anemometer::Anemometer(Timer<>& timer) : Sensor(timer) {}

void Anemometer::run() {
  pinMode(ANEMOMETER_PIN, INPUT);
  timer().every(TICK_INTERVAL, []() -> bool {
    float analog_input = analogRead(ANEMOMETER_PIN);
    float wind_speed = analog_input * 25.0F;

    const char* data = SensorDataSerializer::serialize(ANEMOMETER_ID, SERIALIZER_PROPERTIES, wind_speed);
    Serial.println(data);
    delete[] data;

    return true;
  });
}
