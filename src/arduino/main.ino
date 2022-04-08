#include <Arduino.h>
#include <TMP_38GZ.h>

void setup() {
  Serial.begin(9600);
}

void loop() {
  String serial_data = "[" +
    temperature_sensor_serial_data() +
  "]";

  Serial.println(serial_data);

  delay(1000);
}
