import re

# Regular expression pattern to extract execution time
pattern = r'Execution Time: (\d+\.\d+) sec'

# Initialize variables to store execution times
execution_times = []

# Open the file
with open("C:\\output.txt", 'r') as file:
    # Read each line
    for line in file:
        # Find execution time in the line
        match = re.search(pattern, line)
        if match:
            # Extract execution time
            execution_time = float(match.group(1))
            # Check if execution time is below 10 secs
            if execution_time < 10:
                if len(execution_times) < 20:
                    execution_times.append((execution_time, line.strip()))
                else:
                    # Sort the list and replace the smallest if necessary
                    execution_times.sort(reverse=True)
                    if execution_time > execution_times[-1][0]:
                        execution_times[-1] = (execution_time, line.strip())

# Sort the final list
execution_times.sort(reverse=True)
print("Top 20 execution times below 10 seconds:")
for index, (time, line) in enumerate(execution_times, 1):
    print(f"{index}. Execution Time: {time} seconds, Related line: {line}")