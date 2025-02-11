import os
import pandas as pd

# Paths to `.parquet` files and prompts
PARQUET_DIR = "./GOTBook_op"
PROMPT_DIR = "./prompts"

PARQUET_FILES = {
    "nodes": os.path.join(PARQUET_DIR, "create_final_nodes.parquet"),
    "relationships": os.path.join(PARQUET_DIR, "create_final_relationships.parquet"),
    "entities": os.path.join(PARQUET_DIR, "create_final_entities.parquet"),
    "text_units": os.path.join(PARQUET_DIR, "create_final_text_units.parquet"),
    "community_reports": os.path.join(PARQUET_DIR, "create_final_community_reports.parquet"),
}

PROMPTS = {
    "entity_extraction": os.path.join(PROMPT_DIR, "entity_extraction.txt"),
    "global_search": os.path.join(PROMPT_DIR, "global_search_knowledge_system_prompt.txt"),
    "local_search": os.path.join(PROMPT_DIR, "local_search_system_prompt.txt"),
    "summarization": os.path.join(PROMPT_DIR, "summarize_descriptions.txt"),
    "claim_extraction": os.path.join(PROMPT_DIR, "claim_extraction.txt"),
}

# Load `.parquet` files into DataFrames
dataframes = {key: pd.read_parquet(path) for key, path in PARQUET_FILES.items()}

# Function to load prompts
def load_prompt(prompt_type):
    if prompt_type not in PROMPTS:
        raise ValueError(f"Invalid prompt type: {prompt_type}")
    with open(PROMPTS[prompt_type], "r", encoding="utf-8") as f:
        return f.read()

# Query Functions
def query_entities(query_text):
    """Query entities based on the input text."""
    text_units_df = dataframes["text_units"]
    matches = text_units_df[text_units_df["text"].str.contains(query_text, case=False, na=False)]
    return matches

def summarize_entities(query_text):
    """Summarize the entities using the summarization prompt."""
    entities_df = dataframes["entities"]
    
    # Debug: Print available columns in entities_df
    print("Available columns in entities_df:", entities_df.columns)

    # Filter entities based on the query text
    matches = entities_df[entities_df["title"].str.contains(query_text, case=False, na=False)]
    
    if matches.empty:
        return f"No entities found for the query: {query_text}"

    # Rename 'title' to 'entity_name' to match the prompt
    matches = matches.rename(columns={"title": "entity_name"})
    
    # Load the summarization prompt
    prompt = load_prompt("summarization")
    
    # Format the prompt
    response = prompt.format(entities=matches.to_dict(orient="records"))
    return response

def extract_claims(node_title):
    """Extract claims using the claim extraction prompt."""
    relationships_df = dataframes["relationships"]
    
    # Filter relationships for the given node title
    matches = relationships_df[relationships_df["source"] == node_title]
    
    if matches.empty:
        return f"No claims found for the node: {node_title}"

    # Load the claim extraction prompt
    prompt = load_prompt("claim_extraction")
    
    # Format the prompt
    response = prompt.format(
        claims=matches.to_dict(orient="records"),
        tuple_delimiter=", "  # Add a tuple delimiter if the prompt requires it
    )
    return response

def generate_community_report(node_title):
    """Generate a community report using the community report prompt."""
    nodes_df = dataframes["nodes"]
    community_reports_df = dataframes["community_reports"]

    # Check if the node title exists
    if node_title not in nodes_df["title"].values:
        return f"Node title '{node_title}' not found in nodes."

    # Get the node ID
    node_id = nodes_df.loc[nodes_df["title"] == node_title, "id"].values[0]

    # Filter communities containing the node ID
    communities = community_reports_df[
        community_reports_df["nodes"].apply(lambda nodes: node_id in nodes)
    ]
    
    if communities.empty:
        return f"No community report found for the node: {node_title}"

    # Load the community report prompt
    prompt = load_prompt("community_report")
    
    # Format the prompt
    response = prompt.format(community=communities.to_dict(orient="records"))
    return response

# Interactive Queries
def run_queries():
    """Run queries interactively."""
    print("Query Options:")
    print("1. Query entities")
    print("2. Summarize entities")
    print("3. Extract claims")
    print("4. Generate community report")
    choice = input("Select an option (1/2/3/4): ")

    if choice == "1":
        query_text = input("Enter text to query entities: ")
        results = query_entities(query_text)
        print("\nResults:")
        print(results)

    elif choice == "2":
        query_text = input("Enter text to summarize entities: ")
        results = summarize_entities(query_text)
        print("\nSummary:")
        print(results)

    elif choice == "3":
        node_title = input("Enter node title to extract claims: ")
        results = extract_claims(node_title)
        print("\nClaims:")
        print(results)

    elif choice == "4":
        node_title = input("Enter node title to generate a community report: ")
        results = generate_community_report(node_title)
        print("\nCommunity Report:")
        print(results)

    else:
        print("Invalid choice.")

# Main Execution
if __name__ == "__main__":
    run_queries()
