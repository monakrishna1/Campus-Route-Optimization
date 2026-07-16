// static/project.js

// Leaflet map initialization
var map = L.map('map').setView([13.008269, 80.235010], 15);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors'
}).addTo(map);

function findShortestPath() {
    var startLocation = document.getElementById('startLocation').value;
    var endLocation = document.getElementById('endLocation').value;

    axios.post('/get_shortest_path', { startLocation, endLocation })
        .then(response => {
            var pathCoordinates = response.data.pathCoordinates;
            displayPathOnMap(pathCoordinates);
        })
        .catch(error => console.error(error));
}

function displayPathOnMap(pathCoordinates) {
    // Clear existing layers
    map.eachLayer(function (layer) {
        if (layer instanceof L.Polyline || layer instanceof L.Marker) {
            layer.remove();
        }
    });

    // Add markers for each point
    pathCoordinates.forEach(function (coordinate) {
        L.marker(coordinate).addTo(map);
    });

    // Add polyline to represent the path
    var path = L.polyline(pathCoordinates, { color: 'blue' }).addTo(map);
    map.fitBounds(path.getBounds());
}
