import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV files into a list of DataFrames
stimuli_files = ["Ensure.csv", "CCK.csv", "FACHOW.csv", "FEDCHOW.csv", "FAHF.csv"]
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Calculate the correlation matrices for each stimulus
correlation_matrices = [data.corr() for data in stimuli_data]

# Set up the figure and axes for the grid of heatmaps
fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 10))

# Create a list of axes for each heatmap
ax_list = axs.ravel()

# Draw a heatmap for each stimulus
for i in range(len(stimuli_files)):
    sns.heatmap(correlation_matrices[i], cmap="icefire", vmin=-1, vmax=1, ax=ax_list[i])
    ax_list[i].set_title(
        stimuli_files[i][:-4]
    )  # Use the filename without the .csv extension as the title

# Remove extra axes that aren't used for a heatmap
for ax in ax_list[len(stimuli_files) :]:
    ax.remove()

# Add a title
fig.suptitle("Correlation Heatmaps for All Stimuli")

plt.show()
