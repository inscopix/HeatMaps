import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV files into a list of DataFrames
stimuli_files = ['Ensure.csv', 'Saline.csv', 'IP Dex.csv', 'CCK.csv', 'WSS.csv', 'Oral Dex.csv', 'FACHOW.csv', 'FEDCHOW.csv', 'FAHF.csv', 'EX4.csv', 'LEP.csv']  # Add all your 11 CSV file names
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Calculate the correlation matrices for each stimulus
correlation_matrices = [data.corr() for data in stimuli_data]

# Calculate the mean correlation matrix across all stimuli
mean_correlation_matrix = np.mean(correlation_matrices, axis=0)
mean_correlation_matrix = pd.DataFrame(mean_correlation_matrix, columns=stimuli_data[0].columns, index=stimuli_data[0].columns)

def draw_heatmap(correlation_matrix, title):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="vlag", vmin=-1, vmax=1)
    plt.title(title)
    plt.show()

for i, matrix in enumerate(correlation_matrices, start=1):
    draw_heatmap(matrix, f'Stimulus {i} Correlation Matrix')
    
    # Function to build a graph based on a correlation matrix
def build_graph(correlation_matrix, threshold=0.5):
    G = nx.Graph()

    for i in range(correlation_matrix.shape[0]):
        for j in range(i+1, correlation_matrix.shape[1]):
            if abs(correlation_matrix.iloc[i, j]) >= threshold:
                G.add_edge(i, j, weight=correlation_matrix.iloc[i, j])

    return G

# Build a graph based on the mean correlation matrix
mean_graph = build_graph(mean_correlation_matrix)

def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=800, node_color='skyblue', font_size=10, font_weight='bold', font_color='black')

    edge_widths = [abs(G[u][v]['weight']) * 2 for u, v in G.edges()]
    edge_colors = ['red' if G[u][v]['weight'] < 0 else 'green' for u, v in G.edges()]

    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors, alpha=0.7)

    edge_labels = {(i, j): f"{G[i][j]['weight']:.2f}" for i, j in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title(title)
    plt.show()

# Visualize the mean graph
draw_graph(mean_graph, 'Mean Network Graph across All Stimuli')