import os
import shutil
import time
import json
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete

# Default directory for RAG data and logs
DEFAULT_RAG_DIR = "wikiop"
LOG_FILE = os.path.join(DEFAULT_RAG_DIR, "lightrag.log")  # Log file inside the RAG directory

# Ensure a clean working directory by deleting any existing data
if os.path.exists(DEFAULT_RAG_DIR):
    shutil.rmtree(DEFAULT_RAG_DIR)

# Recreate the working directory
os.mkdir(DEFAULT_RAG_DIR)

# Ensure the log file can be created
if not os.path.exists(DEFAULT_RAG_DIR):
    os.makedirs(DEFAULT_RAG_DIR)  # Create the directory if it doesn't exist

# Configure the working directory for LightRAG
WORKING_DIR = os.environ.get("RAG_DIR", DEFAULT_RAG_DIR)

# Initialize LightRAG with the desired LLM model function and log file
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete,  # Ensure this matches the embedding dimensions
)

# Explicitly set the logger to use the LOG_FILE
from lightrag.utils import set_logger
set_logger(LOG_FILE)

# Function to process a single file
def process_file(file_path):
    stats = {"total_runtime": 0, "steps": {}}
    overall_start = time.time()
    query_results = []

    try:
        # Step 1: Insert document
        step_start = time.time()
        with open(file_path, "r", encoding="utf-8") as f:
            rag.insert(f.read())
        stats["steps"]["insert_document"] = time.time() - step_start
    except Exception as e:
        print(f"Error inserting document {file_path}: {e}")
        stats["steps"]["insert_document_error"] = str(e)

    # Step 2: Perform queries
    queries = [
        ("What are the top themes in this story?", "naive"),
        ("What are the top themes in this story?", "local"),
        ("What are the top themes in this story?", "global"),
        ("What are the top themes in this story?", "hybrid"),
    ]
    for query_text, mode in queries:
        try:
            step_start = time.time()
            result = rag.query(query_text, param=QueryParam(mode=mode))
            query_results.append((mode, result))
            stats["steps"][f"query_{mode}"] = time.time() - step_start
        except Exception as e:
            print(f"Error querying in mode {mode} for file {file_path}: {e}")
            stats["steps"][f"query_{mode}_error"] = str(e)

    # Measure total runtime
    stats["total_runtime"] = time.time() - overall_start

    return stats, query_results

# Directory containing multiple files
input_directory = "./input_files"  # Replace with your directory path
stats_all = {}
query_results_all = {}

# Process each file in the directory
for file_name in os.listdir(input_directory):
    file_path = os.path.join(input_directory, file_name)
    if os.path.isfile(file_path):
        print(f"Processing file: {file_name}")
        try:
            stats, query_results = process_file(file_path)
            stats_all[file_name] = stats
            query_results_all[file_name] = query_results
        except Exception as e:
            print(f"Unexpected error processing file {file_name}: {e}")

# Write stats to stats.json
stats_file_path = os.path.join(DEFAULT_RAG_DIR, "stats_all.json")
print(f"Saving stats to: {stats_file_path}")
try:
    with open(stats_file_path, "w", encoding="utf-8") as stats_file:
        json.dump(stats_all, stats_file, indent=4)
    print("Stats saved successfully.")
except Exception as e:
    print(f"Error saving stats: {e}")

# Print all query results
for file_name, query_results in query_results_all.items():
    print(f"Results for file: {file_name}")
    for mode, result in query_results:
        print(f"  Mode: {mode}\n  Result: {result}\n")
