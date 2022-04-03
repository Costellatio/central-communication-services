#define TEMPERATURE_SENSOR_PIN A0

#define WEATHER_STATION_MEASUREMENT "weather station"

#define TEMPERATURE_FIELD "temperature"

void setup() {
  Serial.begin(9600);
}

void loop() {
  String serial_data = "[" +
    temperature_serial_data() +
  "]";

  Serial.println(serial_data);

  delay(1000); // For Debugging Purposes
}

String build_serial_data(String measurement, String field, String value) {
  String serial_data = "";

  serial_data += "{";
  serial_data +=    "\"measurement\":\"" + measurement + "\",";
  serial_data +=    "\"field\":\""       + field       + "\",";
  serial_data +=    "\"value\":"         + value;
  serial_data += "}";

  return serial_data;
}

String temperature_serial_data() {
  int    sensor_value   = analogRead(TEMPERATURE_SENSOR_PIN);
  float  sensor_voltage = (sensor_value / 1024.0) * 5.0;
  float  value = (sensor_voltage - 0.5) * 100;

  return build_serial_data(WEATHER_STATION_MEASUREMENT, TEMPERATURE_FIELD, String(value));
}
