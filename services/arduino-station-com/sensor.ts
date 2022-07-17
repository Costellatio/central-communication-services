interface InfluxProps {
  measurement: string;
  fields: string[];
}

function getSensorName(id: number): string {
  switch (id) {
  case 1:
    return 'BME280';
  case 2:
    return 'FC37';
  case 3:
    return 'Anemometer';
  case 4:
    return 'MPU6050';
  case 5:
    return 'MLX90614';
  case 6:
    return 'BH1750';
  default:
    return '';
  }
}

function getInfluxProps(id: number): InfluxProps | undefined {
  switch (id) {
  case 1:
    return {
      measurement: 'weather station',
      fields: ['temperature', 'humidity', 'athmosphere pressure', 'altitude'],
    };
  case 2:
    return {
      measurement: 'weather station',
      fields: ['rain'],
    };
  case 3:
    return {
      measurement: 'weather station',
      fields: ['wind speed'],
    };
  case 5:
    return {
      measurement: 'weather station',
      fields: ['difference (ambient - object) temp'],
    };
  case 6:
    return {
      measurement: 'weather station',
      fields: ['light level'],
    };
  default: return undefined;
  }
}

class Sensor {
  name: string;
  props: Record<string, number>;
  influxProps?: InfluxProps;

  constructor(id: number, props: number[]) {
    this.name = getSensorName(id);
    this.influxProps = getInfluxProps(id);

    if (this.influxProps) {
      this.props = this.influxProps.fields.reduce((object, value, index) => {
        object[value] = props[index];
        return object;
      }, {} as Record<string, number>);
    } else {
      this.props = props.reduce((object, value, index) => {
        object[`value${index}`] = value;
        return object;
      }, {} as Record<string, number>);
    }
  }
}

export default Sensor;
