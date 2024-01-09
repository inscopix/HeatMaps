import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# read in the data and set index to 'CellId'
df_props = pd.read_csv("cck_fachow_fedchow_ss_fahf-props.csv")
df_props.set_index("Name", inplace=True)

# create a list of neuron names
neuron_names = [
    "C00",
    "C01",
    "C02",
    "C03",
    "C04",
    "C05",
    "C06",
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

# create a list of correlation matrices, one for each stimulus
correlation_matrices = []
for i in range(1, 6):
    # read in the fluorescence data for the current stimulus and set index to 'Time'
    # filename = f'stimulus_{i}_dff.csv'
    filename = "FACHOW.csv"
    dff = pd.read_csv(filename)
    print(dff.columns)
    # drop the 'Time' column
    # dff = dff.drop(columns=['Time'])
    # set the index to 'Time' and transpose the dataframe
    fluorescence = dff.set_index("Time").T
    # calculate the correlation matrix and add it to the list
    correlation_matrices.append(fluorescence.corr())

# create an empty weighted graph
G = nx.Graph()

# add the nodes to the graph
for name in neuron_names:
    G.add_node(
        name, pos=(df_props.loc[name, "CentroidX"], df_props.loc[name, "CentroidY"])
    )

correlation_matrices[i].columns = correlation_matrices[i].columns.str.strip()

# add the edges to the graph
for i in range(len(correlation_matrices)):
    for j in range(len(neuron_names)):
        for k in range(j + 1, len(neuron_names)):
            # only add edges if the correlation is above a certain threshold

            if abs(correlation_matrices[i].loc[neuron_names[j], neuron_names[k]]) > 0.5:
                G.add_edge(
                    neuron_names[j],
                    neuron_names[k],
                    weight=correlation_matrices[i].loc[
                        neuron_names[j], neuron_names[k]
                    ],
                )

# draw the graph
pos = nx.get_node_attributes(G, "pos")
weights = nx.get_edge_attributes(G, "weight").values()

plt.figure(figsize=(10, 10))
nx.draw_networkx_nodes(G, pos, node_color="white", node_size=500)
nx.draw_networkx_edges(
    G, pos, width=list(weights), edge_color=weights, edge_cmap=plt.cm.coolwarm
)
nx.draw_networkx_labels(
    G, pos, {name: name for name in neuron_names}, font_color="white"
)
plt.axis("off")
plt.show()
