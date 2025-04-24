import serial
from datetime import datetime

# Replace with your Arduino's port
ser = serial.Serial('COM3', 9600)

# Open TXT file for writing
filename = "soil_log_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".txt"
log_file = open(filename, mode='w')

print(f"Logging data to {filename}... Press Ctrl+C to stop.")

try:
    while True:
        line = ser.readline().decode().strip()
        if "Soil moisture" in line:
            try:
                parts = line.split("] ")
                timestamp_str = parts[0].strip("[")
                moisture_str = parts[1].split(": ")[1].replace("%", "")
                moisture = int(moisture_str)

                # Write to file
                log_file.write(f"{timestamp_str}, {moisture}%\n")
                log_file.flush()  # Write immediately to disk

                print(f"{timestamp_str}, {moisture}%")
            except:
                pass
except KeyboardInterrupt:
    print("Stopped logging.")
    log_file.close()
    ser.close()
