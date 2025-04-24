import serial
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your actual port (e.g., 'COM3' or 'COM4')
ser = serial.Serial('COM3', 9600)

timestamps = []
moisture_values = []

plt.ion()  # Interactive mode on
fig, ax = plt.subplots()

while True:
    try:
        line = ser.readline().decode().strip()

        if "Soil moisture" in line:
            parts = line.split("] ")
            timestamp_str = parts[0].strip("[")
            moisture_str = parts[1].split(": ")[1].replace("%", "")

            time = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
            moisture = int(moisture_str)

            timestamps.append(time)
            moisture_values.append(moisture)

            # Keep only last 100 points for performance
            timestamps = timestamps[-100:]
            moisture_values = moisture_values[-100:]

            ax.clear()
            ax.plot(timestamps, moisture_values, label="Soil Moisture (%)")
            ax.set_xlabel("Time")
            ax.set_ylabel("Moisture (%)")
            ax.set_title("Live Soil Moisture Plot")
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.pause(0.1)

    except Exception as e:
        print("Error:", e)
