import os
import pandas as pd
import glob

# Function to merge all CSVs into a single mega.csv
def merge_csv_files(parent_directory, output_file="mega.csv"):
    # Use glob to recursively find all CSV files in the parent directory and subdirectories
    csv_files = glob.glob(os.path.join(parent_directory, '**', '*.csv'), recursive=True)

    # List to hold dataframes
    dataframes = []

    # Read each CSV file and append it to the dataframes list
    for file in csv_files:
        df = pd.read_csv(file)
        dataframes.append(df)

    # Concatenate all dataframes into one
    merged_df = pd.concat(dataframes, ignore_index=True)

    # Save the merged dataframe into a single CSV
    merged_df.to_csv(output_file, index=False)
    print(f"Successfully merged {len(csv_files)} CSV files into {output_file}")

# Replace 'your_parent_directory_path' with the actual parent directory path
parent_directory = r'D:\CODE\projects\python\AmazonML\AmazonML'
output_file = 'mega.csv'

merge_csv_files(parent_directory, output_file)
