import networkx as nx
from pyvis.network import Network
import random

# Load the GraphML file
G = nx.read_graphml(r"E:\CourseWork-Fall-2024\CSE-511-DPS\Project-2\LightRAG\BookOP3\graph_chunk_entity_relation.graphml")

# Create a Pyvis network
net = Network(height="100vh", notebook=True)

# Convert NetworkX graph to Pyvis network
net.from_nx(G)

# Add colors to nodes
for node in net.nodes:
    node["color"] = "#{:06x}".format(random.randint(0, 0xFFFFFF))

# Save and display the network
net.show("knowledge_graph_carol.html")
