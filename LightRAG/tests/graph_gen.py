import networkx as nx
import matplotlib
matplotlib.rcParams['font.family'] = 'DejaVu Sans'  # Use a fallback font
matplotlib.use('Agg')  # Non-interactive backend
import matplotlib.pyplot as plt

# Load the GraphML file
graph = nx.read_graphml("E:/CourseWork-Fall-2024/CSE-511-DPS/Project-2/LightRAG/index_default4/graph_chunk_entity_relation.graphml")

# Plot and save the graph
plt.figure(figsize=(12, 12))
nx.draw(graph, with_labels=True, node_size=500, font_size=10)
plt.title("LightRAG Graph Visualization")
plt.savefig("lightrag_graph_output.png")
print("Graph saved as lightrag_graph_output.png")
