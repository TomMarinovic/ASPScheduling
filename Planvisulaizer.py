import matplotlib.pyplot as plt

# Define colors for different parts
colors = {
    'part_0': 'blue',
    'part_1': 'green',
    'part_2': 'red',
    'part_3': 'orange',
    'part_4': 'purple',
    'part_5': 'brown',
    'part_6': 'pink',
    'part_7': 'gray',
    'part_8': 'cyan',
    'part_9': 'magenta'
}

# Initialize empty lists to store data
cpu_data = {0: [], 1: [], 2: [], 3: []}

# Parse the data and fill the lists
with open("C:\\Users\\marin\\OneDrive\\HTW\\Master\\3. Semester\\FS\\ASP-Scheduler\\schedule3.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if line:  # Skip empty lines
            _, cpu, time_slot, part = line.split('(')[1].split(',')
            cpu = int(cpu)
            time_slot = int(time_slot)
            part = part[:-1]  # remove trailing ')'
            cpu_data[cpu].append((time_slot, part))

# Plot the data
fig, ax = plt.subplots()

for cpu, data in cpu_data.items():
    for time_slot, part in data:
        ax.plot(time_slot, cpu, marker='o', color=colors[part], markersize=8)

ax.set_xlabel('Time Slot')
ax.set_ylabel('CPU')
ax.set_title('CPU Schedule')

# Create legend
legend_elements = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, label=part) 
                   for part, color in colors.items()]
ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))

plt.yticks(list(cpu_data.keys()))  # Set y-axis ticks to CPU numbers
plt.grid(True)
plt.tight_layout()
plt.show()
