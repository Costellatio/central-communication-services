#ifndef SERIAL_DATA_BUILDER_H
#define SERIAL_DATA_BUILDER_H

#include <Arduino.h>
#include <Vector.h>
#include <Tag.h>

class SensorSerialDataBuilder {
  public:
    static String build(String _measurement, String _field, String _value, Vector<Tag> _tags = {});
};

#endif
