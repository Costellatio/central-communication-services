#include "MPU6050.h"
#include <Wire.h>
#include <SensorDataSerializer.h>
#include <SensorIds.h>
#include <SensorInputs.h>

#define TICK_INTERVAL 0.1 * 1000UL
#define ACCELEROMETER_REGISTER 0x3B
#define POWER_MANAGEMENT_REGISTER 0x6B
#define WIRE_REQUEST_SIZE 6
#define SERIALIZER_PROPERTIES 3

MPU6050::MPU6050(Timer<>& timer) : Sensor(timer) {}

void MPU6050::run() {
  Wire.beginTransmission(MPU6050_I2C_ADDRESS);
  Wire.write(POWER_MANAGEMENT_REGISTER);
  Wire.write(0x00);
  Wire.endTransmission();

  timer().every(TICK_INTERVAL, []() -> bool {
    Wire.beginTransmission(MPU6050_I2C_ADDRESS);
    Wire.write(ACCELEROMETER_REGISTER);
    Wire.endTransmission();

    Wire.requestFrom(MPU6050_I2C_ADDRESS, WIRE_REQUEST_SIZE);

    float x = (Wire.read() << 8 | Wire.read()) / 16384.0;
    float y = (Wire.read() << 8 | Wire.read()) / 16384.0;
    float z = (Wire.read() << 8 | Wire.read()) / 16384.0;

    const char* data = SensorDataSerializer::serialize(MPU6050_ID, SERIALIZER_PROPERTIES, x, y, z);
    Serial.println(data);
    delete[] data;

    return true;
  });
}
