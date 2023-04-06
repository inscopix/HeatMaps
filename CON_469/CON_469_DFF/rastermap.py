import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv('CCK.csv')

# Set the figure size
plt.figure(figsize=(10, 5))

plt.eventplot(data.reshape(-1), colors='black')

# Create the raster plot
plt.eventplot(data.T, colors='black')

# Set the x-axis label
plt.xlabel('Time')

# Set the y-axis label
plt.ylabel('Neuron')

# Show the plot
plt.show()
