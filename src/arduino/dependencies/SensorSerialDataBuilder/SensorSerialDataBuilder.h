#ifndef SENSOR_SERIAL_DATA_BUILDER_H
#define SENSOR_SERIAL_DATA_BUILDER_H

#include <Arduino.h>
#include <Tag.h>
#include <Vector.h>

class SensorSerialDataBuilder {
  public:
    static String build(String _measurement, String _field, String _value, Vector<Tag> _tags = {});
};

#endif
