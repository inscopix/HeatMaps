import os
import glob
import pandas as pd
import argparse


def load_csv_files(folder_path):
    # Search for all CSV files in the specified folder
    csv_files = glob.glob(os.path.join(folder_path, "*.csv"))

    # Load the CSV files into a list of DataFrames
    dataframes = [pd.read_csv(file) for file in csv_files]

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
