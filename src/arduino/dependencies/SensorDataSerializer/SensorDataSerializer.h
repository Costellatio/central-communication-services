#ifndef SENSOR_DATA_SERIALIZER_H
#define SENSOR_DATA_SERIALIZER_H

class SensorDataSerializer {
private:
  static const char* stringlify_id(int id);
  static const char* stringlify_property(float property);

public:
  static const char* serialize(int id, int properties_size, ...);
};

#endif
