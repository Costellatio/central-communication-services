#include "BH1750.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

BH1750::BH1750(Timer<>& timer) : Sensor(timer) {}

void BH1750::run() {
  lightMeter.begin()
  timer().every(TICK_INTERVAL, [](BH1750& bh) -> bool {
    float lux = lightMeter.readLightLevel();

    const char* data = SensorDataSerializer::serialize(BH1750_ID, SERIALIZER_PROPERTIES, lux);
    Serial.println(data);
    delete[] data;

    return true;
  }, &bh);
}
