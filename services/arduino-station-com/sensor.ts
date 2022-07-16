interface InfluxProps {
  measurement: string;
  fields: string[];
}

function getInfluxProps(name: string): InfluxProps | undefined {
  switch (name) {
  case 'Anemometer':
    return { measurement: '', fields: [] };
  default:
    return undefined;
  }
}

class Sensor {
  name: string;
  influxProps?: InfluxProps;

  constructor(name: string) {
    this.name = name;
    this.influxProps = getInfluxProps(name);
  }
}

export default Sensor;
