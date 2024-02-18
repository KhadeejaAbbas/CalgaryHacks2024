from flask import Flask, render_template, request, redirect, url_for 
import requests
import csv
import pandas as pd
from io import StringIO
from flask_cors import cross_origin

app = Flask(__name__)



@app.route('/is-parked', methods=['POST'])
@cross_origin()
def parked_app():
    data = request.json
    is_failure = str(update_csv_route( data["address-1"], data["address-2"]))
    return str(is_failure)

@app.route('/availability', methods=['POST'])
@cross_origin()
def available_app():
    data = request.json
    available = str(searchFunctionAddress( data["column_1"], data["column_1"]))
    return available 

def decrement_spot(street_name):
    with open('Dataset_for_map_app_divided.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row['Street'] == street_name:
            available_spots = int(row['Available Spots'])
            if available_spots > 0:
                row['Available Spots'] = str(available_spots - 1)

    with open('parking_data.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def get_spot(street_name):
    with open('Dataset_for_map_app_divided.csv', 'r', newline='') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    for row in rows:
        if row['Street'] == street_name:
            available_spots = int(row['Available Spots'])
            return available_spots


file_url = 'https://raw.githubusercontent.com/KhadeejaAbbas/CalgaryHacks2024/main/Dataset_for_map_app_divided.csv?token=GHSAT0AAAAAACN7XUSWBCKNO6ERCL3JOKJ2ZORXXVQ'  # URL of the CSV file on GitHub
def update_csv_route(column1_value, column2_value):
    # Read the CSV file from GitHub
    df = read_csv_from_github()

    # Call the function to get the return index value
    return_index = searchFunctionAddress(column1_value, column2_value)

    # Decrement the specific column value based on the return index value
    column_to_decrement = 'specific_column'
    df = decrement_column_value(df, return_index, column_to_decrement)

    # Update the CSV file on GitHub
    status_code = update_csv_on_github(df)

    if status_code == 200:
        return 'CSV file updated successfully'
    else:
        return 'Failed to update CSV file', 500
    
# matching_rows_output = searchFunctionAddress(column1_value, column2_value)
# print(matching_rows_output)
def read_csv_from_github():
    response = requests.get(file_url)
    file_content = response.text
    df = pd.read_csv(StringIO(file_content))
    return df

# Function to update the CSV file on GitHub
def update_csv_on_github(df):
    csv_content = df.to_csv(index=False)
    response = requests.put(file_url, data=csv_content)
    return response.status_code

def decrement_column_value(df, index, column_name):
    df.loc[index, column_name] -= 1
    return df

def searchFunctionAddress(column1_value, column2_value):
    
    column1_name = 'First_address'
    column2_name = 'Second_address'
    matching_rows = []

    # Read the CSV file from the GitHub URL using Pandas
    df = pd.read_csv(file_url)

    matching_rows = df[(df[column1_name] == column1_value) & (df[column2_name] == column2_value)]
    column_name = "number_of_spots_left"
    result_values = matching_rows[column_name].tolist()
    return result_values

if __name__ == '__main__':
    app.run(debug=True)
