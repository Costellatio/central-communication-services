#include "MLX90614.h"
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

MLX90614::MLX90614(Timer<>& timer) : Sensor(timer) {}

void MLX90614::run() {
  mlx.begin();
  timer().every(TICK_INTERVAL, [](Adafruit_MLX90614& mlx) -> bool {
    float difference = mlx.readAmbientTempC() - mlx.readObjectTempC(); 

    const char* data = SensorDataSerializer::serialize(MLX90614_ID, SERIALIZER_PROPERTIES, difference);
    Serial.println(data);
    delete[] data;

    return true;
  }, &mlx);
}
