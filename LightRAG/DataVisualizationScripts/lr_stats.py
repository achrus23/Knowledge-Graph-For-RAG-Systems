import os
import shutil
import time
import json
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete

# Default directory for RAG data and logs
DEFAULT_RAG_DIR = "gotbookop"
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

# Rest of the script for document insertion and querying
stats = {"total_runtime": 0, "steps": {}}
overall_start = time.time()

# Step 1: Insert document
step_start = time.time()
with open("./input_files/001ssb.txt", "r", encoding="utf-8") as f:
    rag.insert(f.read())
stats["steps"]["insert_document"] = time.time() - step_start

# Step 2: Perform queries
queries = [
    ("What are the top themes in this story?", "naive"),
    ("What are the top themes in this story?", "local"),
    ("What are the top themes in this story?", "global"),
    ("What are the top themes in this story?", "hybrid"),
]
query_results = []
for query_text, mode in queries:
    step_start = time.time()
    result = rag.query(query_text, param=QueryParam(mode=mode))
    query_results.append((mode, result))
    stats["steps"][f"query_{mode}"] = time.time() - step_start

# Measure total runtime
stats["total_runtime"] = time.time() - overall_start

# Write stats to stats.json
stats_file_path = os.path.join(DEFAULT_RAG_DIR, "stats.json")
print(f"Saving stats to: {stats_file_path}")
try:
    with open(stats_file_path, "w", encoding="utf-8") as stats_file:
        json.dump(stats, stats_file, indent=4)
    print("Stats saved successfully.")
except Exception as e:
    print(f"Error saving stats: {e}")

# Print query results
for mode, result in query_results:
    print(f"Mode: {mode}\nResult: {result}\n")
