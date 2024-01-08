import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def filter_relative_time(
    data, start1=0.25 * 60, end1=1.75 * 60, start2=2.25 * 60, end2=4 * 60
):
    relative_time = data[" Time"] - data[" Time"].iloc[0]
    period1 = data[(relative_time >= start1) & (relative_time <= end1)]
    period2 = data[(relative_time >= start2) & (relative_time <= end2)]
    return pd.concat([period1, period2])


# Function to draw a clustered heatmap for each stimulus
def draw_clustered_heatmap(correlation_matrix):
    g = sns.clustermap(
        correlation_matrix,
        cmap="coolwarm",
        vmin=-1,
        vmax=1,
        row_cluster=True,
        col_cluster=True,
        figsize=(4, 4),
        dendrogram_ratio=0.15,
        cbar_pos=None,
    )
    return g


def clustermapgrid(stimuli_files):
    stimuli_data = [pd.read_csv(file) for file in stimuli_files]
    filtered_data = [filter_relative_time(data) for data in stimuli_data]

    correlation_matrices = [data.corr() for data in filtered_data]

    # Set up the figure for the grid of clustermaps
    fig, axs = plt.subplots(nrows=3, ncols=4, figsize=(20, 10))

    # Create a list of axes for each heatmap
    ax_list = axs.ravel()

    # Iterate through each stimulus file, draw a clustered heatmap,
    # and move its axes to the grid
    for i in range(len(stimuli_files)):
        g = draw_clustered_heatmap(correlation_matrices[i])
        g.ax_heatmap.set_title(stimuli_files[i][:-4], pad=20)
        # Use the filename without the .csv extension as the title

        # Move the heatmap's axes to the grid
        for ax in g.fig.axes:
            ax.set_position(ax_list[i].get_position())
            ax_list[i].set_visible(False)
        g.fig.clf()
        plt.close(g.fig)

    # Add a title
    start1, end1, start2, end2 = 0.25 * 60, 1.75 * 60, 2.25 * 60, 9 * 60
    fig.suptitle(
        f"Clustered Correlation Heatmaps for All Stimuli (Relative Time: {start1 / 60}-{end1 / 60} min and {start2 / 60}-{end2 / 60} min)"
    )

    # Set the visibility of extra axes that aren't used for a heatmap to False
    for ax in ax_list[len(stimuli_files) :]:
        ax.set_visible(False)

    plt.show()
    fig.savefig("clustermapgrid.png")
