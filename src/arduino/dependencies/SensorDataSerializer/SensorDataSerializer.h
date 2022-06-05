#ifndef SENSOR_DATA_SERIALIZER_H
#define SENSOR_DATA_SERIALIZER_H

class SensorDataSerializer {
private:
  static const char* pin_data(int pin);
  static const char* property_data(float property);

public:
  static const char* serialize(int pin, int properties_size, ...);
};

#endif
