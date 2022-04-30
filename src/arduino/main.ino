//#include <Arduino.h>
//#include <TMP_38GZ.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_BME280.h>
#include <SensorSerialDataBuilder.h>

#define SEALEVELPRESSURE_HPA        (1013.25)
#define WEATHER_STATION_MEASUREMENT "weather station"
#define TEMPERATURE_FIELD           "temperature"

Adafruit_BME280 bme;

String temperature_sensor_serial_data() {

  return SensorSerialDataBuilder::build(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(bme.readTemperature()));
}

void setup() {
  Serial.begin(9600);

  if (!bme.begin(0x76)) {
    Serial.println("No BME280 device found!");
    while (1);
  }
}

void loop() {
  // Serial.print("Temperature = ");
  // Serial.print(bme.readTemperature());
  // Serial.println(" °C");
  
  // Serial.print("Pressure = ");
  // Serial.print(bme.readPressure() / 100.0F);
  // Serial.println(" hPa");
  
  // Serial.print("Approx. Altitude = ");
  // Serial.print(bme.readAltitude(SEALEVELPRESSURE_HPA));
  // Serial.println(" m");
  
  // Serial.print("Humidity = ");
  // Serial.print(bme.readHumidity());
  // Serial.println(" %");
  
  // Serial.println();

  String serial_data = "[" +
    temperature_sensor_serial_data() +
  "]";

  Serial.println(serial_data);
  delay(2000);
}
