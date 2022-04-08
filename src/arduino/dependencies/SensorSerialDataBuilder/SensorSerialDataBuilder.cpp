#include "SensorSerialDataBuilder.h"

String SensorSerialDataBuilder::build(String _measurement, String _field, String _value, Vector<Tag> _tags) {
  String serial_sensor_data = "";

  serial_sensor_data += "{";

  serial_sensor_data +=   "\"measurement\":\"" + _measurement + "\",";
  serial_sensor_data +=   "\"field\":\""       + _field       + "\",";
  serial_sensor_data +=   "\"value\":"         + _value       + ",";

  serial_sensor_data +=   "\"tags\":[";
  for (size_t i = 0; i < _tags.size(); i++) {
    serial_sensor_data += "{";
    serial_sensor_data += "\"name\":\"" + _tags[i].name  + "\",";
    serial_sensor_data += "\"value\":"  + _tags[i].value;
    serial_sensor_data += "}";

    if (i < _tags.size() - 1) {
      serial_sensor_data += ",";
    }
  }
  serial_sensor_data +=   "]";

  serial_sensor_data += "}";

  return serial_sensor_data;
}
