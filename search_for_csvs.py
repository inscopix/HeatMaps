import os
import glob
import pandas as pd
import argparse


def load_csv_files(folder_path):
    # Search for all CSV files in the specified folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    # Print the list of CSV files found
    print("CSV files found:")
    for file in csv_files:
        print(os.path.basename(file))

    # Load the CSV files into a list of DataFrames
    dataframes = []
    for file in csv_files:
        df = pd.read_csv(file)

        # Rename the time column to "Time"
        for col_name in df.columns:
            if (
                col_name.strip().lower() == "time"
                or col_name.strip().lower() == "time (s)"
            ):
                df.rename(columns={col_name: "Time"}, inplace=True)

        df.to_csv(file, index=False)

        dataframes.append(df)

    return dataframes


if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Process CSV files in a folder")
    parser.add_argument(
        "folder_path", help="Path to the folder containing the CSV files"
    )

    # Parse arguments
    args = parser.parse_args()

    # Load and process CSV files
    dataframes = load_csv_files(args.folder_path)

    # Continue with your data processing steps
