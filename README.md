# CosApp

### Software Requirements

- docker - [link](https://docs.docker.com/get-docker/)
- docker-compose - [link](https://docs.docker.com/compose/install/)
- python3 - [link](https://www.python.org/downloads/)
- ardoino-ide - [link](https://www.arduino.cc/en/software)
- gcc - [link](https://www.mingw-w64.org/downloads/)

### Hardware Requirements

- Arduino
- Sensors

### Project Setup

```
  # Set Enviroment Variables (Windows Powershell / Unix Shell)
  # Configure the variables to match your system
  >>> cp .env.example .env

  # Download Dependencies
  >>> pip install -r requirements.txt

  # Initialize Project
  >>> invoke initialize-project
```

### Development
```
  # When using new external python libraries
  # Add them to requirements.txt

  # To install newly added Arduino dependencies
  >>> invoke update-arduino-library

  # To start data collection/influx service
  >>> invoke run-influx-service
```
