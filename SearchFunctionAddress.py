import csv

def searchFunctionAddress(file_path, column1_value, column2_value, column1_index, column2_index):
    matching_rows = []

    with open(file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)  # Skip the header row

        for row in reader:
            print(row[column1_index])
            # Check if both column1_value and column2_value exist in the specified columns
            if row[column1_index] == column1_value and row[column2_index] == column2_value:
                print(row[column1_index], row[column2_index])
                matching_rows.append(row)

    return matching_rows

# Example usage:
file_path = 'C:/Users/ayesh/OneDrive/Desktop/Hackathon Project/Dataset_for_map_app_divided1.csv'  # Path to your CSV file
column1_value = '12 Av SW '  # First search string
column2_value = '8 St SW '  # Second search string
column1_index = 10  # Index of the first column to search in
column2_index = 11  # Index of the second column to search in

matching_rows = searchFunctionAddress(file_path, column1_value, column2_value, column1_index, column2_index)
if matching_rows:
    print("Matching rows found:")
    for row in matching_rows:
        print(row)
else:
    print("No matching rows found.")