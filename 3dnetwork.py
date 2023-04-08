import pandas as pd
import networkx as nx
import plotly.graph_objects as go

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

def draw_3d_graph(G, title):
    pos = nx.spring_layout(G, seed=42, dim=3)

    edge_X = []
    edge_Y = []
    edge_Z = []
    for edge in G.edges():
        x0, y0, z0 = pos[edge[0]]
        x1, y1, z1 = pos[edge[1]]
        edge_X += [x0, x1, None]
        edge_Y += [y0, y1, None]
        edge_Z += [z0, z1, None]

    edge_trace = go.Scatter3d(
        x=edge_X, y=edge_Y, z=edge_Z,
        line=dict(width=1, color='gray'),
        mode='lines',
        showlegend=False
    )

    node_X = [pos[node][0] for node in G.nodes()]
    node_Y = [pos[node][1] for node in G.nodes()]
    node_Z = [pos[node][2] for node in G.nodes()]

    node_trace = go.Scatter3d(
        x=node_X, y=node_Y, z=node_Z,
        mode='markers',
        marker=dict(size=6, color='skyblue', line=dict(color='black', width=0.5)),
        text=list(G.nodes()),
        hoverinfo='text',
        showlegend=False
    )

    layout = go.Layout(
        title=title,
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        margin=dict(t=50, b=50, l=50, r=50)
    )

    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)
    fig.show()

for i, (graph, file) in enumerate(zip(stimuli_graphs, stimuli_files), start=1):
    draw_3d_graph(graph, f'{file} Network Graph')