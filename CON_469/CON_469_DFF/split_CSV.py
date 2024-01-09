import pandas as pd

data = pd.read_csv("cck_fachow_fedchow_ss_fahf.csv")


def split_dataframe_on_zeros(df):
    zero_rows = df[df.iloc[:, 1:21].eq(0).all(axis=1)].index.tolist()
    start_indices = [0] + [row + 1 for row in zero_rows]
    end_indices = zero_rows + [len(df)]

    dataframes = []
    for start, end in zip(start_indices, end_indices):
        dataframes.append(df.iloc[start:end, :])

    return dataframes


stimuli_data = split_dataframe_on_zeros(data)

for i, stimulus_data in enumerate(stimuli_data, start=1):
    stimulus_data.to_csv(f"stimulus{i}.csv", index=False)
