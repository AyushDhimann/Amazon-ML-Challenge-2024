import pandas as pd

# Load both CSV files
final_df = pd.read_csv('final.csv')
test_15k_df = pd.read_csv('test_15k.csv')

# Extract only the 'index' column from both DataFrames
final_index = final_df['index']
test_15k_index = test_15k_df['index']

# Find indices in test_15k that are missing in final.csv
missing_indices = test_15k_index[~test_15k_index.isin(final_index)]

if missing_indices.empty:
    print("All index values from test_15k.csv are present in final.csv.")
else:
    print(f"{len(missing_indices)} index values from test_15k.csv are missing in final.csv.")
    # Save missing index values to a CSV file for review (optional)
    missing_indices.to_csv('missing_indices.csv', index=False)
    print("Missing index values have been saved to missing_indices.csv for review.")
