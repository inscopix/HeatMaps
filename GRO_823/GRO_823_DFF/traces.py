import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Replace 'your_file.csv' with the path to your CSV file
csv_file = 'GRO_823_alltimepoints_noamplitude.csv'


# Read the CSV file
df = pd.read_csv(csv_file)
print(df.head())


# Create the raster plot
fig, ax = plt.subplots(figsize=(20, 8))

for index, neuron in enumerate(df.columns[1:]):
    neuron_data = df.loc[df[neuron] == 1]
    ax.plot(neuron_data['Time (s)'], np.ones_like(neuron_data['Time (s)']) * index, '|', markersize=10, label=neuron)

ax.set_xlabel('Time (s)')
ax.set_ylabel('Neurons')
ax.set_title('Raster Plot of Neuron Activity')
ax.set_yticks(range(len(df.columns[1:])))
ax.set_yticklabels(df.columns[1:])
plt.legend()
plt.tight_layout()
plt.show()

