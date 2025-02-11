import json
from collections import Counter
import networkx as nx
import plotly.graph_objects as go
import plotly.io as pio


def load_data(entities_file, relationships_file):
    """Load entities and relationships from JSON files."""
    with open(entities_file, "r") as f:
        entities_data = json.load(f)["data"]
    with open(relationships_file, "r") as f:
        relationships_data = json.load(f)["data"]
    return entities_data, relationships_data


def analyze_entities(entities_data):
    """Analyze and print entity insights."""
    entity_count = len(entities_data)
    print(f"Total number of entities: {entity_count}")
    return entity_count


def analyze_relationships(relationships_data):
    """Analyze and print relationship insights."""
    relationship_count = len(relationships_data)
    print(f"Total number of relationships: {relationship_count}")
    
    # Most common relationship types
    relationship_types = Counter([rel.get("label", "Unknown") for rel in relationships_data])
    print("\nMost common relationship types:")
    for rel_type, count in relationship_types.most_common(5):
        print(f"{rel_type}: {count} times")
    return relationship_count, relationship_types


def find_central_entities(relationships_data):
    """Find and print the most connected entities."""
    connections = Counter()
    for rel in relationships_data:
        connections[rel["src_id"]] += 1
        connections[rel["tgt_id"]] += 1

    most_connected = connections.most_common(5)
    print("\nTop 5 most connected entities:")
    for entity, count in most_connected:
        print(f"{entity}: {count} connections")
    return most_connected


def visualize_graph_plotly(entities_data, relationships_data, output_file="graph_visualization.png"):
    """Visualize the graph using Plotly with positions assigned and save as an image."""
    G = nx.Graph()

    # Add nodes
    for entity in entities_data:
        G.add_node(entity["__id__"], label=entity.get("entity_name", ""))

    # Add edges
    for rel in relationships_data:
        G.add_edge(rel["src_id"], rel["tgt_id"], label=rel.get("label", ""))

    # Generate positions using a layout algorithm
    pos = nx.spring_layout(G)  # You can also try circular_layout, shell_layout, etc.

    # Create Plotly edges and nodes
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    for node, node_data in G.nodes(data=True):
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(node_data.get('label', node))

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        hoverinfo='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            size=10,
            colorbar=dict(
                thickness=15,
                title='Node Connections',
                xanchor='left',
                titleside='right'
            ),
        ),
        text=node_text
    )

    fig = go.Figure(data=[edge_trace, node_trace],
                    layout=go.Layout(
                        title='<br>Knowledge Graph Visualization',
                        titlefont_size=16,
                        showlegend=False,
                        hovermode='closest',
                        margin=dict(b=0, l=0, r=0, t=40),
                        xaxis=dict(showgrid=False, zeroline=False),
                        yaxis=dict(showgrid=False, zeroline=False))
                    )
    
    # Save the graph as an image
    pio.write_image(fig, output_file)
    print(f"Graph saved as {output_file}")

    # Optionally, display the graph
    fig.show()


def main():
    # File paths (update with your file paths)
    entities_file = "./gotbookop/vdb_entities.json"
    relationships_file = "./gotbookop/vdb_relationships.json"

    # Load data
    entities_data, relationships_data = load_data(entities_file, relationships_file)

    # Analyze data
    analyze_entities(entities_data)
    analyze_relationships(relationships_data)
    find_central_entities(relationships_data)

    # Visualize graph using Plotly and save the image
    visualize_graph_plotly(entities_data, relationships_data, output_file="knowledge_graph.png")


if __name__ == "__main__":
    main()
