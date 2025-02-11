import os
import shutil
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete

# Default directory for RAG data
DEFAULT_RAG_DIR = "index_default3"

# Ensure a clean working directory by deleting any existing data
if os.path.exists(DEFAULT_RAG_DIR):
    shutil.rmtree(DEFAULT_RAG_DIR)

# Recreate the working directory
os.mkdir(DEFAULT_RAG_DIR)

# Configure the working directory for LightRAG
WORKING_DIR = os.environ.get("RAG_DIR", DEFAULT_RAG_DIR)

# Initialize LightRAG with the desired LLM model function
rag = LightRAG(
    working_dir=WORKING_DIR,
    llm_model_func=gpt_4o_mini_complete, # Ensure this matches the embedding dimensions
)

# Insert a sample document into the RAG system
with open("./Users/ad/Downloads/ASU/CourseWork/DPS/Project-5-Group-05/book.txt", "r", encoding="utf-8") as f:
    rag.insert(f.read())

# Perform various search queries using LightRAG
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="naive"))
)
print(
    rag.query("Tell me about the book?", param=QueryParam(mode="local"))
)
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="global"))
)
print(
    rag.query("What are the top themes in this story?", param=QueryParam(mode="hybrid"))
)