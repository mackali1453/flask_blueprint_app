# this is distance page
from flask import Blueprint
import networkx as nx 
import osmnx as ox # open source street map for python. 
import haversine as hs # this library allows us to calculate distance between two coordinates
import logging # To save our outputs as .log file 
dashboard = Blueprint('dashboard', __name__) ## Blueprint for distance page. Later this blueprint will be imported by flask app.
@dashboard.route('/dashboard/<name>')
def homepage(name):
    if type(name)!= str: 
        # To test the condition for invalid data.
        raise ValueError("invalid input data")
    logging.basicConfig(filename="output.log",level=logging.CRITICAL,format="%(asctime)s:%(message)s")
    G1 = ox.graph_from_address('MKAD', network_type='drive') #Generate nodes for addresses
    node1 = list(G1.nodes)[0] # Take the first node for input adress. 
    moscow_ring_road = G1.nodes[node1]  # This command allow us to access dictionary which includes coordinates of node
    G2 = ox.graph_from_address(str(name), network_type='drive') 
    node2 = list(G2.nodes)[0] 
    address = G2.nodes[node2] 
    distance = hs.haversine((moscow_ring_road["y"],moscow_ring_road["x"]),(address["y"],address["x"])) # To calculate distance between 2 coordinates
    logging.critical("distance between moscow ring road and {} is {}km".format(name,distance))
    for each1 in list(G1.nodes):
        for each2 in list(G2.nodes):
            # Validate if input address is inside of MKAD by comparing each coordinate of 2 different addresses.
            if (float(str(G1.nodes[each1]["y"])[0:3]),float(str(G1.nodes[each1]["x"])[0:3]))==(float(str(G2.nodes[each2]["y"])[0:3]),float(str(G2.nodes[each2]["x"])[0:3])):
                distance = 0
            else:
                    distance = hs.haversine((moscow_ring_road["y"],moscow_ring_road["x"]),(address["y"],address["x"]))

            
    return str(distance)

              