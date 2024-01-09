import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Set up the figure and axes for the heatmap
fig, ax = plt.subplots(
    nrows=3, ncols=4, figsize=(20, 10), gridspec_kw={"wspace": 0.3, "hspace": 0.4}
)
ax = ax.ravel()

# Draw the heatmaps with no cell labels and a centered colorbar
for i in range(len(stimuli_files)):
    if i == 0:
        sns.heatmap(
            correlation_matrices[i],
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            ax=ax[i],
            cbar_kws={"orientation": "horizontal", "label": "Correlation Coefficient"},
            annot=True,
            fmt=".2f",
            annot_kws={"fontsize": 8},
        )
        ax[i].set_title(stimuli_files[i][:-4], fontsize=14)
    else:
        sns.heatmap(
            correlation_matrices[i],
            cmap="coolwarm",
            vmin=-1,
            vmax=1,
            ax=ax[i],
            cbar=False,
            annot=True,
            fmt=".2f",
            annot_kws={"fontsize": 8},
        )
        ax[i].set_title(stimuli_files[i][:-4], fontsize=14)

    ax[i].tick_params(axis="both", which="major", labelsize=8)

# Set the overall title for the figure
fig.suptitle("Correlation Heatmaps for All Stimuli", fontsize=20)

# Set the font to Helvetica and color to white
# font_manager.fontManager.addfont('/System/Library/Fonts/Helvetica.ttc')
# plt.rcParams['font.family'] = 'Helvetica'
# plt.rcParams['text.color'] = 'white'

# # Set the background to black
# plt.rcParams['axes.facecolor'] = 'black'
# plt.rcParams['figure.facecolor'] = 'black'

plt.show()
