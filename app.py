from flask import Flask, render_template, request, jsonify
import heapq
app = Flask(__name__)
def get_key_by_value(dictionary, search_value):
    for key, value in dictionary.items():
        if search_value.lower() in value.lower():
            return key
    return None

# Dijkstra algorithm with location information
def dijkstra_with_location(graph, node_location, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_node == end:
            path = []
            coordinates = []
            while previous_nodes[current_node] is not None:
                path.append(current_node)
                coordinates.append((node_location[current_node]['lat'], node_location[current_node]['lon']))
                current_node = previous_nodes[current_node]
            path.append(start)
            coordinates.append((node_location[start]['lat'], node_location[start]['lon']))
            return path[::-1], coordinates[::-1], distances[end]
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return None, [], float('infinity')

graph={
    '1':{'2':120,'3':180,'4':90},
    '2':{'1':120,'5':150,'7':270},
    '3':{'1':180,'8':70},
    '4':{'1':90,'9':120},
    '5':{'2':150,'6':70},
    '6':{'5':70,'7':50},
    '7':{'2':270,'6':50,'23':70,'26':230,'29':300},
    '8':{'3':70,'23':50},
    '9':{'4':120,'33':90},
    '23':{'8':50,'7':70,'10':110,'24':220},
    '10':{'11':30,'12':110,'23':110},
    '11':{'10':30,'12':60,'15':160},
    '12':{'10':110,'11':60,'13':30,'30':100},
    '13':{'12':30},
    '15':{'11':130,'16':30,'20':140},
    '16':{'15':30,'17':20},
    '17':{'16':20,'18':70},
    '18':{'17':70,'19':70},
    '19':{'18':70},
    '20':{'15':140,'21':100,'34':130},
    '21':{'20':100,'22':310},
    '22':{'34':100},
    '24':{'23':220},
    '26':{'7':230},
    '27':{'31':90,'32':60},
    '28':{'33':220},
    '29':{'7':300},
    '30':{'12':100},
    '31':{'27':90},
    '32':{'27':60},
    '33':{'28':300,'9':90},
    '34':{'20':130,'22':100}
}

node_name={
    '1':'main gate',
    '2':'two wheeler parking end turning',
    '3':'fountain',
    '4':'car parking end turning',
    '5':'guesthouse',
    '6':'high voltage',
    '7':'transportation engineering',
    '33':'transporation engineering turning',
    '26':'engineering design division',
    '27':'tnea counselling',
    '28':'institute of ocean technology',
    '29':'tamilnadu technology hub',
    '8':'red building',
    '9':'institue of remote sensing',
    '10':'vivekanandh auditorium',
    '11':'department of applied chemistry',
    '12':'alumni associate on ceg',
    '30':'ceg ground',
    '13':'ladies hostel',
    '15':'senior mess',
    '16':'mega mess',
    '17':'pg mess',
    '18':'industry collaboration',
    '19':'health center',
    '20':'ceg hostel turning (right)',
    '21':'ceg hostel',
    '22':'anna centenary library',
    '23':'atm turning',
    '24':'anna central library',
    '25':'anna incubator',
    '31':'tnea counselling turn1',
    '32':'tnea counselling turn2',
    '34':'madras school of economics'
}


node_location={
    '1':{'lat':13.008269,'lon':80.235010},
    '2':{'lat':13.008499,'lon':80.233980},
    '4':{'lat':13.008102,'lon':80.235976},
    '3':{'lat':13.009952,'lon':80.235268},
    '5':{'lat':13.009774,'lon':80.234184},
    '6':{'lat':13.010349,'lon': 80.234367},
    '7':{'lat':13.010851,'lon':80.234442},
    '8':{'lat':13.010694,'lon':80.235407},
    '9':{'lat':13.009210,'lon':80.236169},
    '10':{'lat':13.011363,'lon':80.236437},
    '11':{'lat':13.011927,'lon':80.236427},
    '12':{'lat':13.012858,'lon':80.236673},
    '13':{'lat':13.013401,'lon':80.236770},
    '15':{'lat':13.013799,'lon':80.236834},
    '16':{'lat':13.013616,'lon':80.237655},
    '17':{'lat':13.013563,'lon': 80.238047},
    '18':{'lat':13.013297,'lon':80.238841},
    '19':{'lat':13.013380,'lon':80.239463},
    '20':{'lat':13.014583,'lon':80.236931},
    '21':{'lat':13.014457,'lon':80.238090},
    '22':{'lat':13.017865,'lon':80.238068},
    '23':{'lat':13.010589,'lon':80.236341},
    '24':{'lat':13.010704,'lon':80.238369},
    '25':{'lat': 13.008478,'lon':80.236062},
    '26':{'lat':13.011081,'lon':80.232639},
    '27':{'lat':13.009293,'lon':80.232983},
    '28':{'lat':13.013088,'lon':80.234002},
    '29':{'lat':13.013778,'lon':80.235085},
    '30':{'lat':13.012513,'lon':80.237757},
    '31':{'lat':13.009931,'lon':80.233315},
    '32':{'lat':13.009272,'lon':80.233197},
    '33':{'lat':13.010934,'lon':80.233669},
    '34':{'lat':13.017395,'lon':80.237660}
}

nearby={
    '1':['1'],
    '2':['2','4'],
    '3':['3'],
    '4':['5'],
    '5':['30'],
    '6':['10'],
    '7':['22','24'],
    '8':['15','16','17'],
    '9':['19'],
    '10':['13','21']
}

nodey={
    '1':'exit',
    '2':'parking',
    '3':'fountain',
    '4':'guest house',
    '5':'ground',
    '6':'auditorium',
    '7':'library',
    '8':'mess',
    '9':'health center',
    '10':'hostel'
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_shortest_path', methods=['POST'])
def get_shortest_path():
    data = request.get_json()
    start_location = data['startLocation']
    start_location = get_key_by_value(node_name, start_location)
    end_location = get_key_by_value(node_name, data['endLocation'])

    shortest_path, coordinates, shortest_distance = dijkstra_with_location(graph, node_location, start_location, end_location)

    # Returning the result to the front-end
    response_data = {'pathCoordinates': coordinates, 'shortestDistance': shortest_distance}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)