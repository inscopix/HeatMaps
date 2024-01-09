import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage
from sklearn.preprocessing import StandardScaler
import os

# Change the working directory to the folder containing the script
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the dataset
data = pd.read_csv("Saline.csv")
data = data.dropna()

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Clustering methods
clustering_algorithms = [
    ("Ward", "ward"),
    ("Complete", "complete"),
    ("Average", "average"),
    ("Single", "single"),
]

# Create the linkage matrices for the rows and columns using different clustering methods
for name, method in clustering_algorithms:
    row_linkage = linkage(data_scaled, method=method)
    col_linkage = linkage(data_scaled.T, method=method)

    # Plot the clustermap
    g = sns.clustermap(
        data_scaled,
        row_linkage=row_linkage,
        col_linkage=col_linkage,
        cmap="viridis",
        figsize=(10, 10),
    )
    plt.title(f"Clustermap using {name} linkage")
    plt.show()
