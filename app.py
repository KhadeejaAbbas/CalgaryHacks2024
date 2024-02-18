from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        street_name = request.form['street']
        decrement_spot(street_name)
        return redirect(url_for('index'))
    return render_template('index.html')

def decrement_spot(street_name):
    with open('parking_data.csv', 'r', newline='') as file:
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

if __name__ == '__main__':
    app.run(debug=True)
