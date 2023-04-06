# import pandas as pd
# import matplotlib.pyplot as plt

# # Load the data from CSV
# df = pd.read_csv('CCK.csv')

# # Downsample the data
# k = 18
# df = df.iloc[::k, :]

# # Extract the time column as x-axis
# time = df.iloc[:, 0]

# # Iterate over all other columns and plot them
# for i in range(1, len(df.columns)):
#     plt.plot(time, df.iloc[:, i], label='Column ' + str(i))

# # Set plot title and axis labels
# plt.title('My Line Chart')
# plt.xlabel('Time')
# plt.ylabel('Data Value')

# # Add a legend to show the column names
# plt.legend()

# # Display the plot
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# read in the CSV file
df = pd.read_csv("CCK.csv", names=['col1', 'col2', 'col3'])

# compute baseline fluorescence for each cell based on the first two minutes of the timeframe
baseline = df[df[" Time"] <= 120].groupby('cell').mean()

# subtract the baseline fluorescence from the rest of the traces to get dF/F
dff = df.set_index("cell") - baseline
dff = dff.reset_index()

# ignore a ten second period (2:00-2:10)
dff = dff[(dff["Time"] < 120) | (dff["Time"] >= 130)]

# color each trace blue if its activity increases from baseline and red if its activity decreases
colors = np.where(dff.iloc[:, 2:].diff(axis=0).ge(0), 'blue', 'red')

# plot the traces
fig, ax = plt.subplots(figsize=(10, 6))

for i in range(2, len(dff.columns)):
    ax.plot(dff['Time'], dff.iloc[:, i], color=colors[i-2], linewidth=0.5)

ax.set_xlabel("Time (s)")
ax.set_ylabel("dF/F")
ax.set_title("Traces with Color-Coded Activity")
plt.show()
