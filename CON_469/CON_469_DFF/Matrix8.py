import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV files into a list of DataFrames
stimuli_files = ["Ensure.csv", "CCK.csv", "FACHOW.csv", "FEDCHOW.csv", "FAHF.csv"]
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
    cm = sns.clustermap(correlation_matrices[i], cmap="coolwarm", vmin=-1, vmax=1)
    cm.ax_heatmap.set_title(
        stimuli_files[i][:-4]
    )  # Use the filename without the .csv extension as the title
    cm.ax_heatmap.set_xticklabels(
        cm.ax_heatmap.get_xticklabels(), rotation=45
    )  # Rotate x-axis labels for readability
    cm.ax_heatmap.tick_params(
        left=False, bottom=False
    )  # Hide tick marks on the left and bottom axes

# Remove extra axes that aren't used for a heatmap
for ax in ax_list[len(stimuli_files) * 2 :]:
    ax.remove()

# Add a title
fig.suptitle("Correlation Heatmaps for All Stimuli")

plt.show()
