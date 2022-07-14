#ifndef MLX_90614_H
#define MLX_90614_H

#include <Sensor.h>
#include <Adafruit_MLX90614.h>

class MLX90614 : public Sensor {
private:
  Adafruit_MLX90614 mlx = Adafruit_MLX90614();

public:
  MLX90614(Timer<>& timer);
  void run();
};

#endif
