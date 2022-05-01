#include <WS_BME_280.h>
#include <Adafruit_BME280.h>

Adafruit_BME280 bme;

void setup() {
    Serial.begin(9600);
    while(!Serial);

    bool status = bme.begin(0x76);  

    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!\n");
        while (1) delay(10);
    }
}

void loop() {
  print_weather_station_data(bme);
}
