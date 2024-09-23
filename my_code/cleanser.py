import pandas as pd
import re

# Entity to unit map
entity_unit_map = {
    'width': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'depth': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'height': {'centimetre', 'foot', 'inch', 'metre', 'millimetre', 'yard'},
    'item_weight': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'maximum_weight_recommendation': {'gram', 'kilogram', 'microgram', 'milligram', 'ounce', 'pound', 'ton'},
    'voltage': {'kilovolt', 'millivolt', 'volt'},
    'wattage': {'kilowatt', 'watt'},
    'item_volume': {'centilitre', 'cubic foot', 'cubic inch', 'cup', 'decilitre', 'fluid ounce', 'gallon',
                    'imperial gallon', 'litre', 'microlitre', 'millilitre', 'pint', 'quart'}
}

# Set of all allowed units
allowed_units = {unit for entity in entity_unit_map for unit in entity_unit_map[entity]}

# Function to clean the prediction column
def clean_prediction_column(file_path):
    # Load the mega.csv file into a DataFrame
    df = pd.read_csv(file_path)

    # Define a function to clean individual prediction cells
    def clean_prediction(value):
        # If the cell is NaN or empty, return it as is
        if pd.isna(value) or not isinstance(value, str):
            return ""

        # Split the value into components (words)
        words = value.strip().split()

        # Check if there are exactly two words
        if len(words) != 2:
            return ""

        # Validate the first word as a number (integer or float)
        try:
            num = float(words[0])
        except ValueError:
            return ""  # If not a number, return blank

        # Normalize the second word by removing any trailing slashes
        unit = words[1].rstrip('/').lower()

        # Check if the second word is in the allowed units
        if unit not in allowed_units:
            return ""  # If the unit is not allowed, return blank

        # Return the cleaned "number unit" format
        return f"{num} {unit}"

    # Apply the cleaning function to the "prediction" column
    df['prediction'] = df['prediction'].apply(clean_prediction)

    # Save the cleaned DataFrame back to a new CSV file
    df.to_csv("cleaned_mega.csv", index=False)
    print("Cleaned CSV file saved as cleaned_mega.csv")

# Call the function with your mega.csv file path
clean_prediction_column('mega.csv')
