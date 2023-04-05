import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV files into a list of DataFrames
num_stimuli = 11
stimuli_data = [pd.read_csv(f'stimulus{i}.csv') for i in range(1, num_stimuli + 1)]

# Function to create a raster plot for each stimulus
def plot_raster(stimulus_data, stimulus_number):
    plt.figure(figsize=(15, 5))

    # Iterate over all the neurons (columns) in the DataFrame, excluding the 'Time (s)' column
    for idx, neuron in enumerate(stimulus_data.columns[1:]):
        # Get the spike times for the current neuron
        spike_times = stimulus_data[stimulus_data[neuron] == 1]['Time (s)']
        
        # Plot the spike times as vertical lines at the corresponding neuron's y-coordinate
        plt.vlines(spike_times, idx, idx+1, linewidth=1)

    plt.title(f'Stimulus {stimulus_number} Raster Plot')
    plt.xlabel('Time (s)')
    plt.ylabel('Neurons')
    plt.yticks(range(len(stimulus_data.columns[1:])), stimulus_data.columns[1:])
    plt.xticks(rotation=45)
    plt.show()

# Create a raster plot for each stimulus
for i, stimulus_data in enumerate(stimuli_data, start=1):
    plot_raster(stimulus_data, i)
