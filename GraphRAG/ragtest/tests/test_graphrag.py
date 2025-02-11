import pytest
from graphrag.api.index import build_index
from graphrag.api.query import global_search, local_search
from graphrag.index.graph.visualization.compute_umap_positions import (
    compute_umap_positions,
    get_zero_positions,
)
from graphrag.index.run.run import run_pipeline, run_pipeline_with_config

class TestGraphRAGAPI:
    def test_build_index(self):
        """
        Test the document indexing functionality.
        """
        document = "Alaska is the largest U.S. state by area."
        try:
            index = build_index(document)
            assert index is not None, "Index building failed."
        except Exception as e:
            pytest.fail(f"Index building raised an exception: {e}")

    def test_local_search(self):
        """
        Test the local search functionality.
        """
        query = "Tell me about Alaska."
        try:
            response = local_search(query)
            assert response is not None, "Local search failed to return a result."
        except Exception as e:
            pytest.fail(f"Local search raised an exception: {e}")

    def test_global_search(self):
        """
        Test the global search functionality.
        """
        query = "What is Alaska known for?"
        try:
            response = global_search(query)
            assert response is not None, "Global search failed to return a result."
        except Exception as e:
            pytest.fail(f"Global search raised an exception: {e}")

    
    def test_get_zero_positions(self):
        """
        Test getting zero positions for graph visualization fallback.
        """
        nodes = ["Node1", "Node2"]
        try:
            positions = get_zero_positions(nodes)
            assert len(positions) == len(nodes), "Zero positions generation failed."
        except Exception as e:
            pytest.fail(f"Zero positions computation raised an exception: {e}")


if __name__ == "__main__":
    pytest.main()
