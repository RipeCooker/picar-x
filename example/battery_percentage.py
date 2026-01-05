from robot_hat import ADC

# Initialize ADC on pin A4 (standard for PiCar-X Robot HAT)
battery_pin = ADC("A4")

def get_battery_percentage():
    # Read raw ADC value (0-4095)
    value = battery_pin.read()
    
    # Convert ADC value to actual battery voltage
    # (3.3V reference / 4095 resolution) * 3 (voltage divider ratio)
    voltage = value * 3.3 / 4095 * 3
    
    # Calculate percentage based on 18650 safe range (6.6V empty to 8.4V full)
    percent = (voltage - 6.6) / (8.4 - 6.6) * 100
    
    # Keep result between 0% and 100%
    return max(0, min(100, round(percent, 2))), round(voltage, 2)

percentage, volts = get_battery_percentage()
print(f"Battery: {volts}V ({percentage}%)")
