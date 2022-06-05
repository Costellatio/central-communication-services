#include "SensorSerialDataBuilder.h"
#include <stdlib.h>
#include <string.h>
#include <common.h>
#include <Arduino.h>

char* send_data_integer(int value_enum, int data)
{
    char* buffer = new char[MAX_SIZE_WS_DATA_STORAGE/2];
    char int_number_data[MAX_SIZE_SENSOR_DATA_SIZE];
    char value_enum_data[MAX_SIZE_SENSOR_DATA_SIZE];
    itoa(data, int_number_data, 10);
    itoa(value_enum, value_enum_data, 10);

    strcpy(buffer,value_enum_data);
    strcat(buffer, ",");
    strcat(buffer,int_number_data);
    return buffer;
}
char* send_data_double(int value_enum, double data)
{
    char* buffer = new char[MAX_SIZE_WS_DATA_STORAGE/2];
    char float_number_data[MAX_SIZE_SENSOR_DATA_SIZE];
    char value_enum_data[MAX_SIZE_SENSOR_DATA_SIZE];

    dtostrf(data, FLOAT_NUMBERS_MIN_WIDTH, FLOAT_NUMBERS_RESOLUTION, float_number_data);
    itoa(value_enum, value_enum_data, 10);

    strcpy(buffer, value_enum_data);
    strcat(buffer, ",");
    strcat(buffer, float_number_data);
    return buffer;
}
