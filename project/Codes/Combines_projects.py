import matplotlib.pyplot as plt
from datetime import datetime
import os

# Folder where logs are stored
log_files = {
    "Red Plant": "soil_log_20250423_122054_Red_plant.txt",
    "Lukovina": "soil_log_20250423_153105_Lukovina.txt",
    "Narcis": "soil_log_20250423_183742_Narcis.txt",
    "Beans": "soil_log_20250423_214000_Beans.txt"
}

plt.figure(figsize=(12, 6))

for label, filename in log_files.items():
    timestamps = []
    moisture_values = []

    with open(filename, 'r') as file:
        for line in file:
            try:
                timestamp_str, moisture_str = line.strip().split(", ")
                timestamp = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
                moisture = int(moisture_str.replace("%", ""))

                timestamps.append(timestamp)
                moisture_values.append(moisture)
            except:
                pass  # skip malformed lines

    plt.plot(timestamps, moisture_values, label=label, marker='o')

# Final touches
plt.title("Soil Moisture Comparison for All Plants")
plt.xlabel("Time")
plt.ylabel("Moisture (%)")
plt.ylim(0, 110)
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save the plot
output_path = "C:/Users/Ognjen/Desktop/Sensors and monitoring systems/project/Plots_arduino/moisture_comparison.png"
plt.savefig(output_path)
print(f"Saved combined comparison plot to: {output_path}")

plt.show()
