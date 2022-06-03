#include <WS_BME_280.h>
#include <arduino-timer.h>
#include <common.h>

Adafruit_BME280 bme;
Timer<> ws_timer = timer_create_default();

void setup() {
    Serial.begin(9600);
    while(!Serial);

    bool status = bme.begin(0x76);

    if (!status) {
        Serial.println("Could not find a valid BME280 sensor, check wiring, address, sensor ID!\n");
        while (1) delay(10);
    }
  ws_timer.every(WS_TIME_PERIOD_SECONDS * 1000UL, print_weather_station_data, &bme);
}

void loop() {
  ws_timer.tick();
}
