import pandas as pd

# Load both CSV files
final_df = pd.read_csv('final.csv')
test_15k_df = pd.read_csv('test_15k.csv')

# Ensure that the number of rows in test_15k is equal to or less than in final_df
if len(test_15k_df) <= len(final_df):
    # Update the index column in final.csv with the values from test_15k.csv
    final_df.loc[:len(test_15k_df)-1, 'index'] = test_15k_df['index'].values

    # Save the updated DataFrame back to final.csv
    final_df.to_csv('final.csv', index=False)
    print("The index values from test_15k.csv have been copied to final.csv.")
else:
    print("Error: test_15k.csv has more rows than final.csv. Cannot copy the index values.")
