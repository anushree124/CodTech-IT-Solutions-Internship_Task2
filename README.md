# Codtech_Internship_Task2
# Smart Home Automation System

## Overview
This Smart Home Automation System is a Python-based simulation that demonstrates the functionality of an automated home environment. It allows for the control and monitoring of various smart devices including lights, fans, and thermostats across different rooms in a house.

## Features
- Multiple device type support (lights, fans, thermostats)
- Room-based device organization
- Real-time device status monitoring
- Automated device control
- Adjustable device settings
- Simulated day routine automation

## System Components

### SmartDevice Class
Represents individual smart devices in the home:

#### Device Types
- **Lights**
  - Controllable brightness (0-100%)
  - On/Off functionality
- **Fans**
  - Adjustable speed (0-100%)
  - On/Off functionality
- **Thermostats**
  - Temperature control (in °C)
  - Default temperature: 22°C

#### Device Properties
- `device_id`: Unique identifier
- `device_type`: Type of device
- `room`: Location in the house
- `status`: Current state (ON/OFF)
- Device-specific settings (temperature/brightness/speed)

### SmartHome Class
Main control system for the entire smart home:

#### Key Methods
- `add_device()`: Registers new devices to the system
- `toggle_device()`: Switches devices On/Off
- `adjust_device()`: Modifies device settings
- `get_status()`: Generates comprehensive status report

## Implementation Details

### Device Control
```python
# Adding a new device
home.add_device(SmartDevice("LR_LIGHT", "light", "Living Room"))

# Toggling a device
home.toggle_device("LR_LIGHT")

# Adjusting settings
home.adjust_device("LR_LIGHT", "brightness", 70)
```

### Status Monitoring
The system provides detailed status reports including:
- Timestamp of status check
- Device status per room
- Current settings for each device
- Environmental conditions

## Automated Routines

### Morning Routine
- Turn on living room lights
- Set light brightness to 70%
- Adjust thermostat to 23°C

### Afternoon Settings
- Activate living room fan
- Set fan speed to 60%
- Reduce light brightness to 40%

### Evening Configuration
- Turn on bedroom lights
- Set bedroom brightness to 50%
- Lower thermostat to 22°C

## Sample Usage
```python
# Initialize system
home = SmartHome()

# Configure devices
devices = [
    SmartDevice("LR_LIGHT", "light", "Living Room"),
    SmartDevice("BR_LIGHT", "light", "Bedroom"),
    SmartDevice("LR_FAN", "fan", "Living Room"),
    SmartDevice("THERMO", "thermostat", "Home")
]

# Add devices to system
for device in devices:
    home.add_device(device)

# Control devices
home.toggle_device("LR_LIGHT")
home.adjust_device("THERMO", "temperature", 23)
```

## Simulation Features
- Real-time status updates
- 1-second delay between actions
- Automated sequence of events
- Detailed logging of all actions

## System Requirements
- Python 3.x
- Required libraries:
  - `random`
  - `time`
  - `datetime`

## Customization Options
1. **Device Types**
   - Add new device types
   - Modify existing device properties
   - Create custom device behaviors

2. **Automation Routines**
   - Create custom schedules
   - Define new scenarios
   - Modify timing sequences

3. **Settings**
   - Adjust default values
   - Modify temperature thresholds
   - Customize status reporting

## Future Enhancements
1. **Energy Management**
   - Power consumption monitoring
   - Energy optimization routines
   - Usage statistics

2. **Advanced Features**
   - Motion sensors integration
   - Voice control simulation
   - Mobile app interface
   - Scene creation
   - Schedule management

3. **Additional Functionality**
   - Weather integration
   - Multi-zone control
   - Remote access simulation
   - User permissions
   - Device grouping

## Error Handling
- Device not found handling
- Invalid setting protection
- Status monitoring safeguards
- Value range validation

## Best Practices
1. **Device Naming**
   - Use consistent naming conventions
   - Include room and device type in ID
   - Maintain unique identifiers

2. **System Organization**
   - Group devices by room
   - Maintain logical automation sequences
   - Regular status monitoring

3. **Code Structure**
   - Modular design
   - Clear documentation
   - Consistent formatting

## Documentation
The system includes:
- Detailed status reporting
- Action confirmation messages
- Real-time feedback
- Timestamped events

## Testing
- Device control verification
- Setting adjustment validation
- Status reporting accuracy
- Automation sequence testing

## Support and Maintenance
- Regular status checks
- Setting verification
- System optimization
- Performance monitoring

Output:![image](https://github.com/user-attachments/assets/dd94c19d-fa93-4d2f-9b07-a8e40b565797)
![image](https://github.com/user-attachments/assets/831bdf7b-2a70-41ea-a6e5-5a104f1e6052)
![image](https://github.com/user-attachments/assets/89c18825-521c-4e8a-953b-04b70bc4b8e9)






