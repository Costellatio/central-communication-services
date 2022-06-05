#ifndef SENSOR_DATA_SERIALIZER_H
#define SENSOR_DATA_SERIALIZER_H

class SensorDataSerializer {
private:
  static const char* id_data(int id);
  static const char* property_data(float property);

public:
  static const char* serialize(int pin, int properties_size, ...);
};

#endif
