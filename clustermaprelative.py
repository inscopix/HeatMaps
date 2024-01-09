import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def filter_relative_time(data, start1=0, end1=1.75 * 60, start2=2.25 * 60, end2=4 * 60):
    relative_time = data[" Time"] - data[" Time"].iloc[0]
    period1 = data[(relative_time >= start1) & (relative_time <= end1)]
    period2 = data[(relative_time >= start2) & (relative_time <= end2)]
    return pd.concat([period1, period2])


# Function to draw a clustered heatmap for each stimulus
def draw_clustered_heatmap(correlation_matrix, title):
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
    g.ax_heatmap.set_title(title, pad=20)


def cluster_map_relative(stimuli_files):
    stimuli_data = [pd.read_csv(file) for file in stimuli_files]
    filtered_data = [filter_relative_time(data) for data in stimuli_data]

    correlation_matrices = [data.corr() for data in filtered_data]

    # Iterate through each stimulus file and draw a clustered heatmap
    for i in range(len(stimuli_files)):
        draw_clustered_heatmap(
            correlation_matrices[i], stimuli_files[i][:-4]
        )  # Use the filename without the .csv extension as the title

    plt.show()
    plt.savefig("clustermaprelative.png")
