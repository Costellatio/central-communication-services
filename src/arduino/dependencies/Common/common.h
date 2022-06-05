#ifndef _COMMON_H
#define _COMMON_H

/* Serial data build */
#define MAX_SIZE_SENSOR_DATA_SIZE   12  // Max amount of bytes for single sensor data
#define MAX_SIZE_WS_DATA_STORAGE    64  // Max amount of bytes that can be send at a time from weather station sensors. 
#define FLOAT_NUMBERS_MIN_WIDTH     6   // Example : -1.234 has a width of 6
#define FLOAT_NUMBERS_RESOLUTION    2   // Determines the number of digits after the decimal sign

/* Weather station sensor */
#define WS_TIME_PERIOD_SECONDS      2   // Each N seconds, data from weather station sensors will be sent to serial

#define SEALEVELPRESSURE_HPA        (1013.25)

#define WS_RAIN_SENSOR_1_PIN        A0
#define WS_RAIN_SENSOR_TRESHHOLD    950

enum Sensor_values {
    WS_TEMPERATURE = 10,
    WS_HUMIDITY,
    WS_ATM_PRESSURE,
    WS_ALTITUDE,
    WS_WIND_SENSOR,
    WS_RAIN_SENSOR
};

#endif //_COMMON_H
