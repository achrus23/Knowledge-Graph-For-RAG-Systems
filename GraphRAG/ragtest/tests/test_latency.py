import time
from graphrag.api.index import build_index
from graphrag.api.query import local_search, global_search

def test_indexing_latency():
    document = "Alaska is the largest U.S. state by area." * 1000
    start_time = time.time()
    build_index(document)
    end_time = time.time()
    print(f"Indexing latency: {end_time - start_time:.4f} seconds")
    assert end_time - start_time < 5, "Indexing took too long."

def test_local_query_latency():
    query = "Tell me about Alaska."
    start_time = time.time()
    result = local_search(query)
    end_time = time.time()
    print(f"Local query latency: {end_time - start_time:.4f} seconds")
    assert result, "Local query returned no result."
    assert end_time - start_time < 2, "Local query took too long."

def test_global_query_latency():
    query = "What is Alaska known for?"
    start_time = time.time()
    result = global_search(query)
    end_time = time.time()
    print(f"Global query latency: {end_time - start_time:.4f} seconds")
    assert result, "Global query returned no result."
    assert end_time - start_time < 3, "Global query took too long."
