# Project-5-Group-05
# LightRAG API Server

LightRAG is a FastAPI-based server for Retrieval-Augmented Generation (RAG) operations. It enables seamless interaction with large language models (LLMs) through RESTful HTTP APIs for inserting data, querying, and retrieving information.

---

## **Features**

- **Insert Text or File**: Add data to the RAG index.
- **Query the System**: Retrieve contextual responses using hybrid search modes.
- **REST API**: Provides easy-to-use endpoints.
- **Customizable**: Supports different LLM and embedding models via environment variables.

---

## **Setup Instructions**

### **1. Prerequisites**
- **Python**: Version 3.10 or higher.
- **Conda**: For environment management (optional but recommended).
- **Dependencies**: Installed via `pip`.

---


conda create --name lightrag_env python=3.10 -y
conda activate lightrag_env

pip install fastapi uvicorn pydantic lightrag


chmod +x set_env.sh
./set_env.sh


python examples/lightrag_api_openai_compatible_demo.py
http://0.0.0.0:8020


{
    "query": "Your question here",
    "mode": "hybrid",
    "only_need_context": false
}

1. Query Endpoint
curl -X POST "http://127.0.0.1:8020/query" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is LightRAG?", "mode": "hybrid"}'


{
    "text": "Your text content here"
}
2. Insert Text Endpoint
curl -X POST "http://127.0.0.1:8020/insert" \
     -H "Content-Type: application/json" \
     -d '{"text": "This is a sample document for testing."}'

3. Insert File Endpoint
curl -X POST "http://127.0.0.1:8020/insert_file" \
     -F "file=@path/to/your/file.txt"

4. Health Check Endpoint
curl -X GET "http://127.0.0.1:8020/health"
