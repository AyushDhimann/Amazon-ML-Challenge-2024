import pandas as pd

# Load the existing mega.csv file
df = pd.read_csv('sorted_mega.csv')

# Ensure the DataFrame has an index from 0 to 131287
target_num_rows = 131288

# If the DataFrame has fewer rows, extend it to have 131288 rows
if len(df) < target_num_rows:
    additional_rows = target_num_rows - len(df)
    # Create an empty DataFrame with additional rows
    additional_df = pd.DataFrame({
        'index': range(len(df), target_num_rows),
        'prediction': [''] * additional_rows  # Empty prediction for the new rows
    })
    # Append the additional rows to the original DataFrame
    df = pd.concat([df, additional_df], ignore_index=True)

# Add or update the 'index' column
df['index'] = range(len(df))

# Save the DataFrame to final.csv, keeping existing predictions and adding empty ones if necessary
df.to_csv('final.csv', index=False)

print("final.csv has been created with an index up to 131287 and existing 'prediction' values retained.")
