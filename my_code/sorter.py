import pandas as pd

# Load the CSV file
df = pd.read_csv('cleaned_mega_33.csv')

# Sort the DataFrame by 'group_id' and 'image_link' (alphabetically)
df_sorted = df.sort_values(by=['index'], ascending=[True])

# Save the sorted DataFrame back to a CSV file
df_sorted.to_csv('sorted_mega.csv', index=False)

print("File sorted and saved")
