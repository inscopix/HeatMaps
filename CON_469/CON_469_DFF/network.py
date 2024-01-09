import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Load the CSV files into a list of DataFrames
stimuli_files = ["Ensure.csv", "CCK.csv", "FACHOW.csv", "FEDCHOW.csv", "FAHF.csv"]
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

# Calculate the correlation matrices for each stimulus
correlation_matrices = [data.corr() for data in stimuli_data]

# Create a list of neuron names
neuron_names = [
    "C0",
    "C01",
    "C02",
    "C03",
    "C04",
    "0C5",
    "0C6",
    "C08",
    "C09",
    "C10",
    "C11",
    "C12",
    "C13",
    "C14",
    "C15",
    "C16",
    "C18",
    "C19",
]

# Create a graph for each stimulus
for i in range(len(stimuli_files)):
    # Create an empty graph
    G = nx.Graph()

    # Add the nodes to the graph using the spatial location of the neurons
    for j in range(len(neuron_names)):
        G.add_node(neuron_names[j], pos=(j, i))

    # Add the edges to the graph using the correlation values between the neurons
    for j in range(len(neuron_names)):
        for k in range(j + 1, len(neuron_names)):
            G.add_edge(
                neuron_names[j],
                neuron_names[k],
                weight=correlation_matrices[i].loc[neuron_names[j], neuron_names[k]],
            )

    # Set up the figure
    fig, ax = plt.subplots(figsize=(10, 5))

    # Get the positions of the nodes
    pos = nx.get_node_attributes(G, "pos")

    # Draw the nodes
    nx.draw_networkx_nodes(G, pos, ax=ax)

    # Draw the edges with weights as edge labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edges(G, pos, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    # Add labels for the nodes
    labels = {neuron_names[j]: neuron_names[j] for j in range(len(neuron_names))}
    nx.draw_networkx_labels(G, pos, labels, font_color="w", ax=ax)

    # Set the x and y limits
    ax.set_xlim([-1, len(neuron_names)])
    ax.set_ylim([-1, len(stimuli_files)])

    # Set the title
    ax.set_title(stimuli_files[i][:-4])

    plt.show()
