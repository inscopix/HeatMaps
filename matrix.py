import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

stimuli_files = ['event_aligned_activity.TRACES.csv']  # Add all your 11 CSV file names
stimuli_data = [pd.read_csv(file) for file in stimuli_files]


correlation_matrices = [data.corr() for data in stimuli_data]

def build_graph(correlation_matrix, threshold=0.5):
    G = nx.Graph()

    for i in range(correlation_matrix.shape[0]):
        for j in range(i+1, correlation_matrix.shape[1]):
            if abs(correlation_matrix.iloc[i, j]) >= threshold:
                G.add_edge(i, j, weight=correlation_matrix.iloc[i, j])

    return G

stimuli_graphs = [build_graph(correlation_matrix) for correlation_matrix in correlation_matrices]

def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=200, node_color='skyblue', font_size=10, font_weight='bold', font_color='black')

    edge_widths = [abs(G[u][v]['weight']) * 2 for u, v in G.edges()]
    edge_colors = ['red' if G[u][v]['weight'] < 0 else 'green' for u, v in G.edges()]

    nx.draw_networkx_edges(G, pos, width=edge_widths, edge_color=edge_colors, alpha=0.7)

    edge_labels = {(i, j): f"{G[i][j]['weight']:.2f}" for i, j in G.edges()}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title(title)
    plt.show()

# for i, graph in enumerate(stimuli_graphs, start=1):
#     draw_graph(graph, f'Stimulus {i} Network Graph')

for i, (graph, file) in enumerate(zip(stimuli_graphs, stimuli_files), start=1):
    draw_graph(graph, f'{file} Network Graph')