from lightrag import LightRAG

rag = LightRAG(
    working_dir="./local_neo4j_workdir",
    llm_model_func=None,
    log_level="DEBUG"
)

# Explicitly set Neo4j storage (if supported by the library)
rag.set_kg_storage("Neo4JStorage")


# Test LightRAG initialization
print("LightRAG with Neo4j storage initialized successfully!")
