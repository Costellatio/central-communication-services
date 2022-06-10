#include "FC37.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

#define TICK_INTERVAL 2 * 1000UL
#define SERIALIZER_PROPERTIES 1
#define WS_RAIN_SENSOR_TRESHHOLD 950

FC37::FC37(Timer<>& timer) : Sensor(timer) {}

void FC37::run() {
  pinMode(FC37_PIN, INPUT);
  timer().every(TICK_INTERVAL, []() -> bool {
    int analog_read =  analogRead(FC37_PIN);
    if (analog_read >= WS_RAIN_SENSOR_TRESHHOLD || analog_read == 0)
      return;

    const char* data = SensorDataSerializer::serialize(FC37_ID, SERIALIZER_PROPERTIES, analog_read);
    Serial.println(data);
    delete[] data;

    return true;
  });
}
