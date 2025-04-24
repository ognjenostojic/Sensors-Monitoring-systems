import matplotlib.pyplot as plt
from datetime import datetime
import os

# Folder to save plots
output_folder = "C:/Users/Ognjen/Desktop/Sensors and monitoring systems/project/Plots_arduino"
os.makedirs(output_folder, exist_ok=True)  # Create folder if it doesn't exist

# Your log files
log_files = [
    "soil_log_20250423_122054_Red_plant.txt",
    "soil_log_20250423_153105_Lukovina.txt",
    "soil_log_20250423_183742_Narcis.txt",
    "soil_log_20250423_214000_Beans.txt"
]

for filename in log_files:
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
                pass  # Skip malformed lines

    # Prepare plot
    plt.figure()
    plt.plot(timestamps, moisture_values, marker='o')
    plt.title(f"Soil Moisture: {filename}")
    plt.xlabel("Time")
    plt.ylabel("Moisture (%)")
    plt.ylim(0, 110)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save plot to file
    base_name = os.path.splitext(os.path.basename(filename))[0]
    plot_path = os.path.join(output_folder, f"{base_name}.png")
    plt.savefig(plot_path)
    print(f"Saved plot to {plot_path}")

plt.show()

