import pandas as pd

data = pd.read_csv('con_469_events_alltimepoints_showamplitude.csv')

def split_dataframe_on_time_jumps(df, time_jump_threshold=0.3):
    time_differences = df['Time (s)'].diff()
    jump_rows = time_differences[time_differences > time_jump_threshold].index.tolist()
    start_indices = [0] + jump_rows
    end_indices = jump_rows + [len(df)]

    dataframes = []
    for start, end in zip(start_indices, end_indices):
        dataframes.append(df.iloc[start:end, :])

    return dataframes

stimuli_data = split_dataframe_on_time_jumps(data)

# Print the number of potential new CSVs
num_csvs = len(stimuli_data)
print(f'Preparing to create {num_csvs} new CSV files.')

# Ask for confirmation before proceeding
confirmation = input("Proceed with creating new CSV files? (y/n): ")

if confirmation.lower() == 'y':
    for i, stimulus_data in enumerate(stimuli_data, start=1):
        stimulus_data.to_csv(f'stimulus{i}.csv', index=False)
    print("New CSV files created.")
else:
    print("Operation canceled.")
