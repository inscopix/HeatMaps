import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set plot style parameters
plt.rcParams['font.family'] = 'Helvetica'
plt.rcParams['font.size'] = 10  # Adjust the value for a smaller font size
plt.rcParams['axes.labelsize'] = 10  # Adjust the value for the desired axes font size

# Read the CSV files into a list of DataFrames
stimuli_files = ['Ensure.csv', 'CCK.csv', 'FACHOW.csv', 'FEDCHOW.csv', 'FAHF.csv']
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Function to create a raster plot for each stimulus
def plot_raster(ax, stimulus_data, stimulus_number):
    # Generate colors for each neuron
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(stimulus_data.columns[1:])))
    # Set time to start from 0 for each stimulus
    stimulus_data['Time (s)'] = stimulus_data['Time (s)'] - stimulus_data['Time (s)'].iloc[0]
    
    # Iterate over all the neurons (columns) in the DataFrame, excluding the 'Time (s)' column
    for idx, (neuron, color) in enumerate(zip(stimulus_data.columns[1:], colors)):
        # Get the spike times for the current neuron
        spike_times = stimulus_data[stimulus_data[neuron] == 1]['Time (s)']
        
        # Plot the spike times as vertical lines at the corresponding neuron's y-coordinate
        ax.vlines(spike_times, idx, idx+1, colors=color, linewidth=1)

    # Set titles and labels for the plot
    ax.set_title(f'Stimulus {stimulus_number} Raster Plot', color='white')
    ax.set_xlabel('Time (s)', color='white')
    ax.set_ylabel('Neurons', color='white')
    ax.set_yticks(range(len(stimulus_data.columns[1:])))
    ax.set_yticklabels(stimulus_data.columns[1:], color='white')
    ax.tick_params(axis='x', rotation=0, colors='white')
    
    # Set plot appearance parameters
    ax.spines[:].set_visible(False)
    ax.set_facecolor('black')
    ax.patch.set_edgecolor('white')
    ax.patch.set_linewidth(1)
    # Update the y-axis tick labels font size
    ax.set_yticklabels(ax.get_yticklabels(), fontsize=8)  # Change the value '8' to your desired font size

# Create a raster plot for each stimulus
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(10, 10), constrained_layout=True)
ax_list = axs.ravel()
fig.patch.set_facecolor('black')

# Plot each stimulus and set the title
for i, stimulus_data in enumerate(stimuli_data):
    plot_raster(ax_list[i], stimulus_data, i)
    ax_list[i].set_title(stimuli_files[i][:-4], color='white')  # Use the filename without the .csv extension as the title

# Remove unused axes
for ax in ax_list[len(stimuli_data):]:
    ax.remove()

plt.tight_layout()
plt.show()
