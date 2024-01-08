import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import (
    KMeans,
    DBSCAN,
    MeanShift,
    AgglomerativeClustering,
    SpectralClustering,
    OPTICS,
)
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Change the working directory to the folder containing the script
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the dataset
data = pd.read_csv("Ensure.csv")
data = data.dropna()

# Standardize the data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Reduce dimensionality using PCA for visualization purposes
pca = PCA(n_components=2)
data_2D = pca.fit_transform(data_scaled)

# Clustering methods
clustering_algorithms = [
    ("K-means", KMeans(n_clusters=3)),
    ("DBSCAN", DBSCAN(eps=0.5, min_samples=5)),
    ("Mean Shift", MeanShift()),
    ("Agglomerative Clustering", AgglomerativeClustering(n_clusters=3)),
    ("Spectral Clustering", SpectralClustering(n_clusters=3)),
    ("Gaussian Mixture", GaussianMixture(n_components=3)),
    ("OPTICS", OPTICS(min_samples=5)),
]

# Plotting
fig, axs = plt.subplots(2, 4, figsize=(20, 10), sharex=True, sharey=True)
axs = axs.ravel()

for i, (name, algorithm) in enumerate(clustering_algorithms):
    # Fit the clustering algorithm
    if name == "Gaussian Mixture":
        algorithm.fit(data_scaled)
        labels = algorithm.predict(data_scaled)
    else:
        algorithm.fit(data_scaled)
        labels = algorithm.labels_

    # Visualize the results
    sns.scatterplot(
        x=data_2D[:, 0],
        y=data_2D[:, 1],
        hue=labels,
        palette="viridis",
        ax=axs[i],
        legend=None,
    )
    axs[i].set_title(name)

# Remove unused subplot
axs[-1].axis("off")

plt.suptitle('Comparison of Clustering Algorithms on "Ensure.csv"', fontsize=20, y=1.05)
plt.tight_layout()
plt.show()
