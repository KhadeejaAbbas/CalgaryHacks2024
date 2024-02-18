let parkingData = []; // Global variable to store parsed CSV data

document.getElementById('csvFileInput').addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const contents = e.target.result;
            parkingData = processData(contents);
        };
        reader.readAsText(file);
    }
});

document.getElementById('checkInButton').addEventListener('click', function() {
    const searchTerm = document.getElementById('searchInput').value.trim().toLowerCase();
    if (searchTerm === '') {
        alert('Please enter a street name.');
        return;
    }
    
    const streetData = parkingData.find(entry => entry.street.toLowerCase() === searchTerm);
    if (!streetData) {
        alert('Street not found in the CSV file.');
        return;
    }

    const availableSpots = parseInt(streetData.available_spots);
    if (availableSpots > 0) {
        streetData.available_spots = (availableSpots - 1).toString();
        document.getElementById('searchResults').innerText = `You have successfully checked into the parking lot on ${streetData.street}.`;
    } else {
        alert('Sorry, there are no available spots on this street.');
    }
});

function processData(csvText) {
    const lines = csvText.split('\n');
    const headers = lines[0].split(',');
    const data = [];
    for (let i = 1; i < lines.length; i++) {
        const line = lines[i].split(',');
        if (line.length === headers.length) {
            const entry = {};
            for (let j = 0; j < headers.length; j++) {
                entry[headers[j].trim()] = line[j].trim();
            }
            data.push(entry);
        }
    }
    return data;
}
