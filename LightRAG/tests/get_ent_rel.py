import networkx as nx

# Load the graph
G = nx.read_graphml(r"location\of\graphml")

# Function to get all edges and nodes with properties
def get_all_edges_and_nodes(G):
    # Get all edges and their properties
    edges_with_properties = []
    for u, v, data in G.edges(data=True):
        edges_with_properties.append(
            {
                "start": u,
                "end": v,
                "label": data.get("label", ""),  # Assuming 'label' is used for edge type
                "properties": data,
                "start_node_properties": G.nodes[u],
                "end_node_properties": G.nodes[v],
            }
        )
    return edges_with_properties

if __name__ == "__main__":
    # Get the number of nodes and edges
    num_nodes_entities = G.number_of_nodes()
    num_edges_relationships = G.number_of_edges()
    

    print(f"Number of nodes: {num_nodes_entities}")
    print(f"Number of edges: {num_edges_relationships}")

    # Get all edges with their properties
    all_edges = get_all_edges_and_nodes(G)

    #Print all edges and node properties
    for edge in all_edges:
        print(f"Edge Label: {edge['label']}")
        print(f"Edge Properties: {edge['properties']}")
        print(f"Start Node: {edge['start']}")
        print(f"Start Node Properties: {edge['start_node_properties']}")
        print(f"End Node: {edge['end']}")
        print(f"End Node Properties: {edge['end_node_properties']}")
        print("---")
