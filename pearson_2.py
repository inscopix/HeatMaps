import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def calculate_correlation(a, b):
    return pearsonr(a, b)[0]


def compare_activity(neuron_data, period1, period2, threshold):
    colors = []
    for activity in neuron_data.T:
        diff = np.mean(activity[period2]) - np.mean(activity[period1])
        if diff > threshold:
            colors.append("red")
        elif diff < -threshold:
            colors.append("blue")
        else:
            colors.append("black")
    return colors


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
                G.add_edge(i, j)

    node_colors = compare_activity(
        neuron_activity, period1, period2, activity_threshold
    )

    return G, node_colors


def visualize_graph(G, node_colors):
    pos = nx.get_node_attributes(G, "pos")
    nx.draw(G, pos, node_color=node_colors, with_labels=True)
    plt.show()


# Example dataset
coordinates = [(0, 1), (1, 2), (2, 1), (1, 0)]
time_points = 100
neurons = 4
neuron_activity = np.random.rand(time_points, neurons)

# Periods and thresholds
period1 = slice(0, 50)
period2 = slice(50, 100)
corr_threshold = 0.5
activity_threshold = 0.1

# Create and visualize the graph
G, node_colors = create_graph(
    coordinates, neuron_activity, corr_threshold, period1, period2, activity_threshold
)
visualize_graph(G, node_colors)
