import os

import pandas as pd
import matplotlib.pyplot as plt

script_folder = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_folder)

# Load the CSV data
data = pd.read_csv("cck_fachow_fedchow_ss_fahf-props.csv")

# Invert the y-axis
plt.gca().invert_yaxis()

# Set the background color
plt.gca().set_facecolor("black")

# Plot the scatter points with colors from the CSV
plt.scatter(
    data["CentroidX"],
    data["CentroidY"],
    c=data[["ColorR", "ColorG", "ColorB"]].apply(
        lambda x: [c / 255 for c in x], axis=1
    ),
    alpha=0.5,
)

# Add axis labels and title
plt.xlabel("CentroidX")
plt.ylabel("CentroidY")
plt.title("Scatter plot of CentroidX and CentroidY with RGB colors from CSV")

# Show the plot
plt.show()
