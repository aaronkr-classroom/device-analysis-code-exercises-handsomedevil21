from room_sensor import RoomSensor

# Create objects
sensor1 = RoomSensor("Kitchen", 31, 72, 180)
sensor2 = RoomSensor("Bedroom", 24, 50, 300)
sensor3 = RoomSensor("Balcony", 18, 35, 150)

# Store in list
sensors = [sensor1, sensor2, sensor3]

# Counters
comfortable = 0
normal = 0
warning = 0

# Loop through sensors
for sensor in sensors:
    sensor.show_info()
    
    level = sensor.comfort_level()
    light = sensor.light_status()
    
    print(f"Comfort Level: {level}")
    print(f"Light Status: {light}")
    print("-" * 30)

    # Count categories
    if level == "Comfortable":
        comfortable += 1
    elif level == "Normal":
        normal += 1
    elif level == "Warning":
        warning += 1

# Print totals
print("Summary:")
print(f"Comfortable: {comfortable}")
print(f"Normal: {normal}")
print(f"Warning: {warning}")