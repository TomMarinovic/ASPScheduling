import re
import matplotlib.pyplot as plt
import numpy as np

# Regular expression pattern to extract relevant data
pattern = r'Timeouts: (\d+), Errors: (\d+), SATs: (\d+), UNSATs: (\d+), Execution Time: (\d+\.\d+) sec'

# Initialize cumulative counts for SATs and UNSATs
sat_cumulative_sum = np.zeros(11)
unsat_cumulative_sum = np.zeros(11)

# Open the file
with open("C:\\output.txt", 'r') as file:
    # Read each line
    for line in file:
        # Find relevant data in the line
        match = re.search(pattern, line)
        if match:
            # Extract data
            timeout, _, sat, unsat, execution_time = map(float, match.groups())
            execution_time = float(execution_time)
            # Check if execution time is within 0 to 10 seconds
            if 2 <= execution_time <= 10:
                # Calculate bin index
                bin_index = int(execution_time)
                # Accumulate counts for the current bin and all previous bins
                sat_cumulative_sum[:bin_index+1] += sat
                unsat_cumulative_sum[:bin_index+1] += unsat

# Plotting histograms
plt.figure(figsize=(10, 6))

# Plotting SAT
plt.plot(range(11), sat_cumulative_sum, label='Cumulative SATs', color='g')

# Plotting UNSAT
plt.plot(range(11), unsat_cumulative_sum, label='Cumulative UNSATs', color='r')

plt.xlabel('Time (seconds)')
plt.ylabel('Cumulative Count')
plt.title('Cumulative Distribution of SAT and UNSAT over Execution Time (0-10 seconds)')
plt.legend()
plt.tight_layout()
plt.show()
