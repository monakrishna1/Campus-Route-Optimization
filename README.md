# Campus Route Optimization System

## Overview
The Campus Route Optimization System is a web-based application designed to help users find the shortest and most efficient route between different locations within a college campus.

The system uses the Dijkstra shortest path algorithm to calculate the optimal path and displays the route visually on an interactive map interface.

## Features
- Find the shortest path between two campus locations.
- Interactive map visualization using Leaflet Maps.
- Displays route distance and path information.
- Fast and efficient path calculation using Dijkstra Algorithm.
- User-friendly web interface.
- Real-time route visualization.

## Technologies Used
- Python
- Flask
- HTML
- CSS
- JavaScript
- Leaflet.js
- Priority Queue (Heap)
- Dijkstra Algorithm

## Project Structure

```
Campus-Route-Optimization/
│
├── app.py
├── index.html
├── static/
├── templates/
├── images/
└── README.md
```

## Algorithm Used

### Dijkstra Algorithm
The project uses Dijkstra's algorithm to determine the shortest path between the selected source and destination locations.

The algorithm:
1. Assigns an initial distance to all nodes.
2. Selects the node with the minimum distance.
3. Updates neighboring node distances.
4. Repeats until the destination node is reached.
5. Returns the optimal route and total distance.

## Installation

### Clone the Repository

```bash
git clone https://github.com/monakrishna1/Campus-Route-Optimization.git
```

### Navigate to the Project Folder

```bash
cd Campus-Route-Optimization
```

### Install Dependencies

```bash
pip install flask
```

### Run the Application

```bash
python app.py
```

### Open in Browser

```
http://127.0.0.1:5000
```

## Usage
1. Select the source location.
2. Select the destination location.
3. Click the route search button.
4. View the shortest route on the map.
5. Check the total distance and path information.

## Applications
- College campuses
- Universities
- Corporate campuses
- Hospitals
- Industrial parks
- Smart city navigation systems

## Future Enhancements
- Real-time traffic information.
- Multiple transportation modes.
- Estimated travel time calculation.
- GPS integration.
- Mobile application support.

## Contributors
- Mona K

## License
This project is developed for educational and academic purposes.
