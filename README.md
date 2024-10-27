# Codtech_Internship_Task2
# IoT Weather Monitoring Station

## Overview
This project implements a WiFi-enabled weather monitoring station using a MicroPython-based microcontroller (like ESP32 or ESP8266) and a BME280 environmental sensor. The system collects temperature, pressure, and humidity data and transmits it to a cloud platform for remote monitoring.

## Features
- Real-time environmental monitoring
- WiFi connectivity
- Cloud data transmission (ThingSpeak integration)
- Automated readings every 5 minutes
- BME280 sensor integration for:
  - Temperature (°C)
  - Atmospheric Pressure (hPa)
  - Relative Humidity (%)

## Hardware Requirements
1. **Microcontroller**
   - ESP32 or ESP8266 board
   - USB cable for programming

2. **Sensor**
   - BME280 Environmental sensor
   - I2C interface compatibility

3. **Connections**
   - SCL (Pin 22)
   - SDA (Pin 21)
   - 3.3V power supply
   - Ground

## Software Dependencies
- MicroPython firmware
- Required libraries:
  - `machine`: For hardware interface
  - `network`: For WiFi functionality
  - `urequests`: For HTTP requests
  - `bme280`: BME280 sensor driver
  - `time`: For timing functions
  - `json`: For data formatting

## Installation

1. **Flash MicroPython**
   - Download and flash MicroPython firmware to your board

2. **Install Required Libraries**
   - Upload the BME280 library to your board
   - Transfer the main script to your board

3. **Configuration**
   Replace the following placeholders in the code:
   ```python
   WIFI_SSID = "YOUR_WIFI_SSID"
   WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"
   API_KEY = "YOUR_THINGSPEAK_API_KEY"
   ```

## Functionality

### WiFi Connection
```python
def connect_wifi():
    # Establishes WiFi connection
    # Returns network configuration
```

### Sensor Reading
```python
def read_sensor():
    # Reads BME280 sensor data
    # Returns dictionary with:
    # - Temperature (°C)
    # - Pressure (hPa)
    # - Humidity (%)
    # - Timestamp
```

### Data Transmission
```python
def send_data(data):
    # Sends data to ThingSpeak
    # Uses HTTP GET request
    # Includes error handling
```

## Data Format
The system collects and transmits data in the following format:
```python
{
    'temperature': float,  # in Celsius
    'pressure': float,    # in hPa
    'humidity': float,    # in percentage
    'timestamp': int      # Unix timestamp
}
```

## Cloud Platform Integration
The project uses ThingSpeak as the default cloud platform:
- Field 1: Temperature
- Field 2: Pressure
- Field 3: Humidity

## Operation
1. System initializes and connects to WiFi
2. Every 5 minutes:
   - Reads sensor data
   - Displays readings locally
   - Transmits data to ThingSpeak
   - Waits for next cycle

## Error Handling
- WiFi connection errors
- Sensor reading failures
- Data transmission issues
- All errors are logged to console

## Customization Options
1. **Sampling Rate**
   - Modify `time.sleep(300)` for different intervals

2. **Cloud Platform**
   - Modify `send_data()` to use different platforms

3. **Sensor Configuration**
   - I2C pins can be modified in initialization
   - Additional sensor parameters can be added

## Power Management
- Designed for continuous operation
- Can be modified for battery operation
- Consider deep sleep for battery preservation

## Troubleshooting
1. **WiFi Issues**
   - Check credentials
   - Verify signal strength
   - Monitor connection status

2. **Sensor Problems**
   - Verify I2C connections
   - Check power supply
   - Monitor sensor readings

3. **Data Transmission**
   - Verify API key
   - Check internet connectivity
   - Monitor response codes

## Future Enhancements
1. Battery monitoring
2. Deep sleep implementation
3. Local data storage
4. Web interface
5. Additional sensors
6. Alert system

## Safety Notes
- Ensure proper power supply
- Protect from moisture
- Verify pin connections
- Consider environmental factors

