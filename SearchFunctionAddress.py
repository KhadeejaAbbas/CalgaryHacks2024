import csv
import pandas as pd

def searchFunctionAddress(file_url, column1_value, column2_value, column1_index, column2_index):
    matching_rows = []

    # Read the CSV file from the GitHub URL using Pandas
    df = pd.read_csv(file_url)

    matching_rows = df[(df[column1_name] == column1_value) & (df[column2_name] == column2_value)]

    return matching_rows

# Example usage:
github_file_url = 'https://raw.githubusercontent.com/KhadeejaAbbas/CalgaryHacks2024/main/Dataset_for_map_app_divided.csv?token=GHSAT0AAAAAACN7XUSWBCKNO6ERCL3JOKJ2ZORXXVQ'  # URL of the CSV file on GitHub

column1_value = '12 Av SW '  # First search string
column2_value = '8 St SW '  # Second search string
column1_name = 'First_address'  # Name of the first column to search in
column2_name = 'Second_address'  # Name of the second column to search in

matching_rows = searchFunctionAddress(github_file_url, column1_value, column2_value, column1_name, column2_name)
if not matching_rows.empty:
    print("Matching rows found:")
    print(matching_rows)
else:
    print("No matching rows found.")