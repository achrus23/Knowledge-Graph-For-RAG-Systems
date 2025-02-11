from fastapi import FastAPI, HTTPException, Request
from lightrag import LightRAG, QueryParam
from pydantic import BaseModel
from lightrag.llm import gpt_4o_mini_complete

rag = LightRAG(
    working_dir="./rag_dir",
    llm_model_func=gpt_4o_mini_complete,  # Replace this with your desired LLM function
    log_level="DEBUG"
)


app = FastAPI()

# Initialize LightRAG instance
rag = LightRAG(
    working_dir="./rag_dir",
    llm_model_func=None,  # Replace with your LLM function
)

# Input models
class QueryRequest(BaseModel):
    query: str
    mode: str = "hybrid"  # Options: naive, local, global, hybrid
    only_need_context: bool = False

class InsertRequest(BaseModel):
    text: str

# Endpoints
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/query")
async def query_rag(request: QueryRequest):
    try:
        response = rag.query(
            request.query,
            param=QueryParam(mode=request.mode, only_need_context=request.only_need_context)
        )
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/insert")
async def insert_text(request: InsertRequest):
    try:
        rag.insert(request.text)
        return {"status": "success", "message": "Text inserted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
