import os
import json
import requests

# Constants
WORKING_DIR = "./index_default2"
BATCH_SIZE_NODES = 500
BATCH_SIZE_EDGES = 100

# Neo4j HTTP connection credentials
NEO4J_HTTP_URI = "http://localhost:7474"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "password"

# Headers for the Neo4j REST API
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}


def convert_xml_to_json(xml_path, output_path):
    """Converts XML file to JSON and saves the output."""
    if not os.path.exists(xml_path):
        print(f"Error: File not found - {xml_path}")
        return None

    # Use a utility function to convert XML to JSON
    from lightrag.utils import xml_to_json  # Import here to avoid issues if unused
    json_data = xml_to_json(xml_path)
    if json_data:
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, ensure_ascii=False, indent=2)
        print(f"JSON file created: {output_path}")
        return json_data
    else:
        print("Failed to create JSON data")
        return None


def execute_query(query, parameters=None):
    """Executes a Cypher query using the Neo4j HTTP REST API."""
    payload = {
        "statements": [
            {
                "statement": query,
                "parameters": parameters or {},
            }
        ]
    }

    response = requests.post(
        NEO4J_HTTP_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD), headers=HEADERS, json=payload
    )

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None


def process_in_batches(query, data, batch_size, key):
    """Processes data in batches and executes the query."""
    for i in range(0, len(data), batch_size):
        batch = data[i : i + batch_size]
        parameters = {key: batch}
        result = execute_query(query, parameters)
        if result:
            print(f"Processed batch with {len(batch)} items.")
        else:
            print("Error processing batch.")


def main():
    # Paths
    xml_file = os.path.join(WORKING_DIR, "graph_chunk_entity_relation.graphml")
    json_file = os.path.join(WORKING_DIR, "graph_data.json")

    # Convert XML to JSON
    json_data = convert_xml_to_json(xml_file, json_file)
    if json_data is None:
        return

    # Load nodes and edges
    nodes = json_data.get("nodes", [])
    edges = json_data.get("edges", [])

    # Neo4j Cypher queries
    create_nodes_query = """
    UNWIND $nodes AS node
    MERGE (e:Entity {id: node.id})
    SET e.entity_type = node.entity_type,
        e.description = node.description,
        e.source_id = node.source_id,
        e.displayName = node.id
    """

    create_edges_query = """
    UNWIND $edges AS edge
    MATCH (source {id: edge.source})
    MATCH (target {id: edge.target})
    MERGE (source)-[r:RELATIONSHIP {description: edge.description}]->(target)
    SET r.keywords = edge.keywords, r.weight = edge.weight
    """

    # Insert nodes and edges in batches
    process_in_batches(create_nodes_query, nodes, BATCH_SIZE_NODES, "nodes")
    process_in_batches(create_edges_query, edges, BATCH_SIZE_EDGES, "edges")


if __name__ == "__main__":
    main()
