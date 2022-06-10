# CosApp

### Software Requirements

- docker - [link](https://docs.docker.com/get-docker/)
- docker-compose - [link](https://docs.docker.com/compose/install/)
- python3 - [link](https://www.python.org/downloads/)
- arduino-ide - [link](https://www.arduino.cc/en/software)
- gcc - [link](https://www.mingw-w64.org/downloads/)

### Hardware Requirements

- Arduino
- Sensors

### Project Setup

```
  # Set Enviroment Variables (Windows Powershell / Unix Shell)
  >>> cp .env.example .env
  # Configure the uninitialized variables to match your system

  # Download Dependencies
  >>> pip install -r requirements.txt

  # Initialize Project
  >>> invoke initialize-project
```

### Base Development Rules

```
  # When using new external python libraries
  # !!! Add them to requirements.txt !!!

  # To update all dependencies when working
  >>> invoke install-dependencies

  # To start the serial communication service
  >>> invoke start-serial-processor
```

### Sensor Development Concepts

```
  # Define a Sensor Id and Sensor Pin/I2C Address
  # Implement the sensor logic in a timer task
  # Serialize the output and print to Serial
  # Wrap the sensor call in a toggle
  # Create a sensor class handler for the serial services to handle
  # Match the sensor class handler to the id in the klass mapper
```
