import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the CSV files into a list of DataFrames
stimuli_files = [
    "Ensure.csv",
    "Saline.csv",
    "IP Dex.csv",
    "CCK.csv",
    "WSS.csv",
    "Oral Dex.csv",
    "FACHOW.csv",
    "FEDCHOW.csv",
    "FAHF.csv",
    "EX4.csv",
    "LEP.csv",
]


def filter_relative_time(data, start1=0, end1=1.75, start2=2.25, end2=5):
    relative_time = data[" Time"] - data[" Time"].iloc[0]
    period1 = data[(relative_time >= start1) & (relative_time <= end1)]
    period2 = data[(relative_time >= start2) & (relative_time <= end2)]
    return pd.concat([period1, period2])


def minutes(stimuli_files):
    stimuli_data = [pd.read_csv(file) for file in stimuli_files]

    filtered_data = [filter_relative_time(data) for data in stimuli_data]

    filtered_data = [filter_relative_time(data) for data in stimuli_data]

    # Calculate the correlation matrices for each stimulus
    correlation_matrices = [data.corr() for data in filtered_data]

    # Set up the figure and axes for the grid of heatmaps
    fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 10))

    # Create a list of axes for each heatmap
    ax_list = axs.ravel()

    # Draw a heatmap for each stimulus
    for i in range(len(stimuli_files)):
        sns.heatmap(
            correlation_matrices[i], cmap="coolwarm", vmin=-1, vmax=1, ax=ax_list[i]
        )
        ax_list[i].set_title(
            stimuli_files[i][:-4]
        )  # Use the filename without the .csv extension as the title

    # Remove extra axes that aren't used for a heatmap
    for ax in ax_list[len(stimuli_files) :]:
        ax.remove()

    # Add a title
    fig.suptitle("(data, start1=0.25*60, end1=1.75*60, start2=2.25*60, end2=3*60)")

    plt.show()
    fig.savefig("minutes.png")
