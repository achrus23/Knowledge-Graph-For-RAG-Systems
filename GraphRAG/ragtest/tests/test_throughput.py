import pytest
import asyncio
import time
from graphrag.api.query import local_search
from graphrag.api.config import GraphRagConfig

@pytest.mark.asyncio
async def test_throughput():
    # Prepare the configuration object with Parquet file paths
    config = GraphRagConfig(
        nodes="./output/final_nodes.parquet",
        entities="./output/final_entities.parquet",
        community_reports="./output/final_community_reports.parquet",
        text_units="./output/final_text_units.parquet",
        relationships="./output/final_relationships.parquet",
        query="Tell me about Jon Snow."
    )

    # Create multiple queries for throughput testing
    configs = [config] * 50  # Create 50 copies of the configuration object

    start_time = time.time()

    # Run queries concurrently
    await asyncio.gather(*(local_search(cfg) for cfg in configs))

    end_time = time.time()

    elapsed_time = end_time - start_time
    assert elapsed_time > 0, "Elapsed time is zero, adjust test workload."

    throughput = len(configs) / elapsed_time
    print(f"Throughput: {throughput:.2f} queries/second")
    assert throughput > 10, "Throughput is too low."
