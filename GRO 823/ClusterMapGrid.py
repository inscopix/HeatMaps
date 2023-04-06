import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV files into a list of DataFrames
stimuli_files = ['Ensure.csv', 'Saline.csv', 'IP Dex.csv', 'CCK.csv', 'WSS.csv', 'Oral Dex.csv', 'FACHOW.csv', 'FEDCHOW.csv', 'FAHF.csv', 'EX4.csv', 'LEP.csv']
stimuli_data = [pd.read_csv(file) for file in stimuli_files]

def filter_relative_time(data, start1=0, end1=119, start2=128, end2=168):
    relative_time = data[' Time'] - data[' Time'].iloc[0]
    period1 = data[(relative_time >= start1) & (relative_time <= end1)]
    period2 = data[(relative_time >= start2) & (relative_time <= end2)]
    return pd.concat([period1, period2])

filtered_data = [filter_relative_time(data) for data in stimuli_data]
correlation_matrices = [data.iloc[:, 1:].corr() for data in stimuli_data]

fig = plt.figure(figsize=(20, 10))

label_fontsize = 5  # Adjust this value to change the size of x-axis and y-axis labels
title_fontsize = 12  # Adjust this value to change the size of the title

for i in range(len(stimuli_files)):
    row, col = i // 4, i % 4
    ax = plt.subplot2grid((3, 4), (row, col), fig=fig)
    
    data = correlation_matrices[i]
    cm = sns.clustermap(data, cmap="coolwarm", vmin=-1, vmax=1, cbar=False)
    
    # Move the heatmap to the desired location in the grid
    ax.imshow(cm.data2d, cmap="coolwarm", vmin=-1, vmax=1)
    ax.set_xticks(np.arange(data.shape[1]))
    ax.set_xticklabels(data.columns[cm.dendrogram_col.reordered_ind], rotation=45, fontsize=label_fontsize)
    ax.set_yticks(np.arange(data.shape[0]))
    ax.set_yticklabels(data.index[cm.dendrogram_row.reordered_ind], fontsize=label_fontsize)
    ax.set_title(stimuli_files[i][:-4], pad=5, fontsize=title_fontsize)
    
    # Close the newly created figure by seaborn (we only need the heatmap)
    plt.close(cm.fig)

fig.suptitle('Correlation Heatmaps for All Stimuli', fontsize=16)

plt.show()
