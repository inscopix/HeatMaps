import os
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import pandas as pd

script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load neuron_activity and coordinates data from CSV files
neuron_activity = pd.read_csv('CCK.csv', header=0, index_col=0).to_numpy()
coordinates = pd.read_csv('cck_fachow_fedchow_ss_fahf-props.csv', usecols=['CentroidX', 'CentroidY'], header=0).to_numpy()

# Periods and thresholds
period1 = slice(0, 1200)
period2 = slice(1400, 4000)
activity_threshold = 0.4

def calculate_correlation(a, b):
    return pearsonr(a, b)[0]

def calculate_activity_differences(neuron_activity, period1, period2):
    activity_differences = []
    for activity in neuron_activity.T:
        diff = np.mean(activity[period2]) - np.mean(activity[period1])
        activity_differences.append(diff)
    return activity_differences

activity_differences = calculate_activity_differences(neuron_activity, period1, period2)

import matplotlib.colors as mcolors

cmap = plt.get_cmap('seismic')
node_norm = mcolors.Normalize(vmin=min(activity_differences), vmax=max(activity_differences))
node_colors = [cmap(node_norm(diff)) for diff in activity_differences]

def create_graph(coordinates, neuron_activity, corr_threshold, period1, period2, activity_threshold):
    G = nx.Graph()
    
    n = neuron_activity.shape[1]
    for i in range(n):
        G.add_node(i, pos=coordinates[i])

    for i in range(n):
        for j in range(i+1, n):
            correlation = calculate_correlation(neuron_activity[:, i], neuron_activity[:, j])
            if correlation > corr_threshold:
                G.add_edge(i, j, weight=correlation)

    return G, node_colors

def visualize_graph(ax, G, node_colors):
    pos = nx.get_node_attributes(G, 'pos')
    edge_colors = [G[u][v]['weight'] for u, v in G.edges()]
    cmap = plt.get_cmap('gist_yarg')
    edge_norm = mcolors.Normalize(vmin=-1, vmax=1)

    nx.draw(G, pos, node_color=node_colors, with_labels=True, font_color='white',
            edge_color=cmap(edge_norm(edge_colors)), edge_cmap=cmap, edge_vmin=-1, edge_vmax=1, ax=ax)
    ax.set_facecolor('black')

# Create two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))

# Create and visualize the graphs with different correlation thresholds
corr_threshold_1 = 0.5
G1, node_colors1 = create_graph(coordinates, neuron_activity, corr_threshold_1, period1, period2, activity_threshold)
visualize_graph(ax1, G1, node_colors1)
ax1.set_title(f'Correlation Threshold: {corr_threshold_1}')
# plt.gca().invert_yaxis()

corr_threshold_2 = 0.8
G2, node_colors2 = create_graph(coordinates, neuron_activity, corr_threshold_2, period1, period2, activity_threshold)
visualize_graph(ax2, G2, node_colors2)
ax2.set_title(f'Correlation Threshold: {corr_threshold_2}')
# plt.gca().invert_yaxis()
plt.show()

