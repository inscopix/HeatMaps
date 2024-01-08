import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd

script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load neuron_activity and coordinates data from CSV files
neuron_activity = pd.read_csv("CCK.csv", header=0, index_col=0).to_numpy()
coordinates = pd.read_csv(
    "cck_fachow_fedchow_ss_fahf-props.csv", usecols=["CentroidX", "CentroidY"], header=0
).to_numpy()

# Periods and thresholds
period1 = slice(0, 1200)
period2 = slice(1400, 8000)
activity_threshold = 0.9


def calculate_correlation(a, b):
    return pearsonr(a, b)[0]


def calculate_activity_differences(
    neuron_activity, period1, period2, activity_threshold
):
    activity_differences = []
    for activity in neuron_activity.T:
        activity_filtered = activity[np.abs(activity) > activity_threshold]
        diff = np.mean(activity_filtered[period2]) - np.mean(activity_filtered[period1])
        activity_differences.append(diff)
    return activity_differences


activity_differences = calculate_activity_differences(
    neuron_activity, period1, period2, activity_threshold
)


import matplotlib.colors as mcolors

cmap = plt.get_cmap("coolwarm")
node_norm = mcolors.Normalize(
    vmin=min(activity_differences), vmax=max(activity_differences)
)
node_colors = [cmap(node_norm(diff)) for diff in activity_differences]


def create_graph(
    coordinates, neuron_activity, corr_threshold, period1, period2, activity_threshold
):
    G = nx.Graph()

    n = neuron_activity.shape[1]
    for i in range(n):
        G.add_node(i, pos=coordinates[i])

    for i in range(n):
        for j in range(i + 1, n):
            correlation = calculate_correlation(
                neuron_activity[:, i], neuron_activity[:, j]
            )
            if correlation > corr_threshold:
                G.add_edge(i, j, weight=correlation)

    # Calculate node colors based on activity_threshold
    activity_differences = calculate_activity_differences(
        neuron_activity, period1, period2, activity_threshold
    )
    node_colors = []
    for diff in activity_differences:
        if diff > activity_threshold:
            node_colors.append(cmap(1.0))
        elif diff < -activity_threshold:
            node_colors.append(cmap(0.0))
        else:
            node_colors.append(cmap(0.5))

    return G, node_colors


def visualize_graph(ax, G, node_colors):
    pos = nx.get_node_attributes(G, "pos")
    edge_colors = [G[u][v]["weight"] for u, v in G.edges()]
    cmap = plt.get_cmap("gist_yarg")
    edge_norm = mcolors.Normalize(vmin=-1, vmax=1)

    nx.draw(
        G,
        pos,
        node_color=node_colors,
        with_labels=True,
        font_color="white",
        edge_color=cmap(edge_norm(edge_colors)),
        edge_cmap=cmap,
        edge_vmin=-1,
        edge_vmax=1,
        ax=ax,
    )
    ax.invert_yaxis()  # Invert the y-axis
    ax.set_facecolor("black")


# Create a 5x5 grid of subplots
n_rows = 5
n_cols = 5
fig, axes = plt.subplots(n_rows, n_cols, figsize=(25, 25))
fig.subplots_adjust(hspace=0.5, wspace=0.5)

# Define the range of corr_threshold and activity_threshold values
corr_thresholds = np.linspace(0.1, 1, n_rows)
activity_thresholds = np.linspace(0.1, 1, n_cols)

# Loop through the subplots and corr_threshold values
for i, corr_threshold in enumerate(corr_thresholds):
    for j, activity_threshold in enumerate(activity_thresholds):
        # Create and visualize the graph with the current corr_threshold and activity_threshold values
        G, node_colors = create_graph(
            coordinates,
            neuron_activity,
            corr_threshold,
            period1,
            period2,
            activity_threshold,
        )
        visualize_graph(axes[i, j], G, node_colors)
        axes[i, j].set_title(
            f"Corr. Thresh.: {corr_threshold:.2f}, Act. Thresh.: {activity_threshold:.2f}"
        )

# Display the final figure
plt.show()
