#include <Arduino.h>
#include "WS_Rain_Sensor.h"
#include <Wire.h>
#include <SensorSerialDataBuilder.h>
#include <common.h>

void read_rain_sensor()
{
    int analog_read =  analogRead(WS_RAIN_SENSOR_1_PIN);
    if (analog_read >= WS_RAIN_SENSOR_TRESHHOLD || analog_read == 0)
        return;

    char serial_data[MAX_SIZE_WS_DATA_STORAGE];
    char *rain_sensor = send_data_integer(WS_RAIN_SENSOR, analog_read);

    strcpy(serial_data, "#");
    strcat(serial_data, rain_sensor);
    strcat(serial_data, "#");
    // if you want to add more sensors use strcat()

    delete[] rain_sensor;
    Serial.println(serial_data);
}
