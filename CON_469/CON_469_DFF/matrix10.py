import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("cck_fachow_fedchow_ss_fahf-props.csv")

fig, ax = plt.subplots(figsize=(10, 10))

ax.set_facecolor("black")
ax.invert_yaxis()

plt.scatter(
    data["CentroidX"],
    data["CentroidY"],
    c=list(zip(data["ColorR"] / 255, data["ColorG"] / 255, data["ColorB"] / 255)),
    alpha=0.9,
    s=500,
)

for i, row in data.iterrows():
    plt.text(row["CentroidX"], row["CentroidY"] + 10, f"C{i}", color="white")

plt.show()
