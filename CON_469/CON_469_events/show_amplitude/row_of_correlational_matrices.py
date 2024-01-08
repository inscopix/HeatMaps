import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Change the working directory to the folder containing the script
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the CSV files into a list of DataFrames
stimuli_files = [
    "Ensure.csv",
    "CCK.csv",
    "FACHOW.csv",
    "FEDCHOW.csv",
    "FAHF.csv",
]  # Add all your 11 CSV file names
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Calculate the correlation matrices for each stimulus
correlation_matrices = [data.corr() for data in stimuli_data]

# Combine the correlation matrices into a single DataFrame
combined_matrix = pd.concat(correlation_matrices, axis=1)

# Set up the figure and axes for the heatmap
fig, ax = plt.subplots(figsize=(20, 10))

# Draw the heatmap with no cell labels and a centered colorbar
sns.heatmap(
    combined_matrix,
    cmap="magma",
    vmin=-1,
    vmax=1,
    ax=ax,
    cbar_kws={"orientation": "horizontal", "label": "Correlation Coefficient"},
)
ax.set_title("Correlation Heatmap for All Stimuli")
ax.tick_params(bottom=False, left=False)

plt.show()
