import pandas as pd
import re

# Load the CSV file
df = pd.read_csv('D:/CODE/projects/python/AmazonML/student_resource 3/dataset/train.csv')

# Function to remove numbers and whitespaces, convert to lowercase
def clean_entity_value(value):
    # Remove numbers and decimal points
    value = re.sub(r'\d+(\.\d+)?', '', value)
    # Convert to lowercase
    value = value.lower()
    # Remove whitespaces
    value = value.replace(" ", "")
    return value

# Apply the clean function to 'entity_value' column
df['entity_value_cleaned'] = df['entity_value'].astype(str).apply(clean_entity_value)

# Get unique values from the cleaned 'entity_value' column
unique_entity_values = df['entity_value_cleaned'].unique()

# Print the unique cleaned values
print("Unique cleaned values in 'entity_value' column:")
print(unique_entity_values)

# Sort the DataFrame by 'group_id' and 'image_link' (alphabetically)
df_sorted = df.sort_values(by=['group_id', 'image_link'], ascending=[True, True])

# Save the sorted DataFrame back to a CSV file
df_sorted.to_csv('dataset/uniquetrain.csv', index=False)

print("File sorted and saved")
