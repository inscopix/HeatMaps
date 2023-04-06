import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV files into a list of DataFrames
stimuli_files = ['Ensure.csv', 'CCK.csv', 'FACHOW.csv', 'FEDCHOW.csv', 'FAHF.csv']
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Calculate the correlation matrices for each stimulus, excluding the 'Time' column
correlation_matrices = [data.iloc[:, 1:].corr() for data in stimuli_data]

# Set up the figure and axes for the grid of heatmaps
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 10))

# Create a list of axes for each heatmap
ax_list = axs.ravel()

# Draw a heatmap for each stimulus
for i in range(len(stimuli_files)):
    # Use the clustermap function to sort the order of the cells
    cm = sns.clustermap(correlation_matrices[i], cmap="viridis", vmin=-1, vmax=1, ax=ax_list[i])
    cm.ax_heatmap.set_title(stimuli_files[i][:-4])  # Use the filename without the .csv extension as the title
    cm.ax_heatmap.set_xticklabels(cm.ax_heatmap.get_xticklabels(), rotation=45)  # Rotate x-axis labels for readability
    cm.ax_heatmap.tick_params(left=False, bottom=False)  # Hide tick marks on the left and bottom axes

    # Add labels to the dendrogram
    dendrogram_row = cm.dendrogram_row.reordered_ind
    for idx, label in enumerate(correlation_matrices[i].columns[dendrogram_row]):
        cm.ax_row_dendrogram.text(-0.01, idx, label, ha='right', va='center', fontsize=8)

    dendrogram_col = cm.dendrogram_col.reordered_ind
    for idx, label in enumerate(correlation_matrices[i].index[dendrogram_col]):
        cm.ax_col_dendrogram.text(idx, -0.01, label, ha='center', va='top', fontsize=8)

# Remove extra axes that aren't used for a heatmap
for ax in ax_list[len(stimuli_files)*2:]:
    ax.remove()

# Add a title
fig.suptitle('Correlation Heatmaps for All Stimuli')

plt.show()
