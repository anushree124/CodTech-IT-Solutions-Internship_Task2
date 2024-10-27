# IoT Weather Monitoring Station
from machine import Pin, I2C
import time
import network
import urequests
import json
from bme280 import BME280  # BME280 sensor library

# WiFi Configuration
WIFI_SSID = "YOUR_WIFI_SSID"
WIFI_PASSWORD = "YOUR_WIFI_PASSWORD"

# Initialize I2C for BME280 sensor
i2c = I2C(1, scl=Pin(22), sda=Pin(21))
bme = BME280(i2c=i2c)

# Connect to WiFi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to WiFi...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print('WiFi connected!')
    print('Network config:', wlan.ifconfig())

# Read sensor data
def read_sensor():
    try:
        temperature = bme.temperature
        pressure = bme.pressure
        humidity = bme.humidity
        
        return {
            'temperature': round(temperature, 2),
            'pressure': round(pressure, 2),
            'humidity': round(humidity, 2),
            'timestamp': time.time()
        }
    except Exception as e:
        print('Sensor reading error:', e)
        return None

# Send data to server (you can modify this to use your preferred platform)
def send_data(data):
    try:
        # Example using ThingSpeak
        API_KEY = "YOUR_THINGSPEAK_API_KEY"
        url = f"https://api.thingspeak.com/update?api_key={API_KEY}"
        url += f"&field1={data['temperature']}"
        url += f"&field2={data['pressure']}"
        url += f"&field3={data['humidity']}"
        
        response = urequests.get(url)
        response.close()
        print('Data sent successfully')
    except Exception as e:
        print('Error sending data:', e)

# Main loop
def main():
    connect_wifi()
    
    while True:
        data = read_sensor()
        if data:
            print('Sensor readings:')
            print(f"Temperature: {data['temperature']}°C")
            print(f"Pressure: {data['pressure']} hPa")
            print(f"Humidity: {data['humidity']}%")
            
            send_data(data)
        
        time.sleep(300)  # Wait 5 minutes before next reading

if __name__ == '__main__':
    main()