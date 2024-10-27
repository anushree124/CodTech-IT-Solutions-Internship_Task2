import random
import time
from datetime import datetime

class SmartDevice:
    def __init__(self, device_id, device_type, room):
        self.device_id = device_id
        self.device_type = device_type
        self.room = room
        self.status = "OFF"
        self.temperature = 22 if device_type == "thermostat" else None
        self.brightness = 0 if device_type == "light" else None
        self.speed = 0 if device_type == "fan" else None

class SmartHome:
    def __init__(self):
        self.devices = {}
        self.temperature_threshold = 24
        
    def add_device(self, device):
        self.devices[device.device_id] = device
        print(f"Added {device.device_type} in {device.room}")
    
    def toggle_device(self, device_id):
        if device_id in self.devices:
            device = self.devices[device_id]
            device.status = "ON" if device.status == "OFF" else "OFF"
            return f"{device.device_type} in {device.room} turned {device.status}"
        return "Device not found"
    
    def adjust_device(self, device_id, setting, value):
        if device_id in self.devices:
            device = self.devices[device_id]
            if setting == "temperature" and device.device_type == "thermostat":
                device.temperature = value
            elif setting == "brightness" and device.device_type == "light":
                device.brightness = value
            elif setting == "speed" and device.device_type == "fan":
                device.speed = value
            return f"Adjusted {device.device_type} in {device.room} - {setting}: {value}"
        return "Device not found"

    def get_status(self):
        status = f"\nHome Status at {datetime.now().strftime('%H:%M:%S')}\n"
        status += "-" * 50 + "\n"
        
        for device in self.devices.values():
            status += f"{device.room} {device.device_type}:\n"
            status += f"  Status: {device.status}\n"
            
            if device.temperature is not None:
                status += f"  Temperature: {device.temperature}°C\n"
            if device.brightness is not None:
                status += f"  Brightness: {device.brightness}%\n"
            if device.speed is not None:
                status += f"  Speed: {device.speed}%\n"
            
        return status

def simulate_smart_home():
    # Initialize smart home
    home = SmartHome()
    
    # Add devices
    devices = [
        SmartDevice("LR_LIGHT", "light", "Living Room"),
        SmartDevice("BR_LIGHT", "light", "Bedroom"),
        SmartDevice("LR_FAN", "fan", "Living Room"),
        SmartDevice("THERMO", "thermostat", "Home")
    ]
    
    for device in devices:
        home.add_device(device)
    
    print("\nStarting Smart Home Simulation...")
    print("=" * 50)
    
    # Simulate some automated actions
    actions = [
        # Morning routine
        ("LR_LIGHT", "toggle"),
        ("LR_LIGHT", "brightness", 70),
        ("THERMO", "temperature", 23),
        # Afternoon adjustments
        ("LR_FAN", "toggle"),
        ("LR_FAN", "speed", 60),
        ("LR_LIGHT", "brightness", 40),
        # Evening settings
        ("BR_LIGHT", "toggle"),
        ("BR_LIGHT", "brightness", 50),
        ("THERMO", "temperature", 22)
    ]
    
    # Execute actions with delays
    for i, action in enumerate(actions, 1):
        print(f"\nAction {i}:")
        if len(action) == 2:
            device_id, command = action
            result = home.toggle_device(device_id)
        else:
            device_id, setting, value = action
            result = home.adjust_device(device_id, setting, value)
        
        print(result)
        print(home.get_status())
        time.sleep(1)  # 1 second delay between actions
    
    print("\nSimulation complete!")

if __name__ == "__main__":
    simulate_smart_home()
