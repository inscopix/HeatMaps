import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Change the working directory to the folder containing the script
script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

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

