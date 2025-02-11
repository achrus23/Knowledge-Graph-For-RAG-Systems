import psutil
import time
from graphrag.api.index import build_index

def test_cpu_usage():
    document = "Alaska is the largest U.S. state by area." * 10000
    start_time = time.time()
    build_index(document)
    end_time = time.time()
    cpu_percent = psutil.cpu_percent(interval=1)
    print(f"CPU usage during indexing: {cpu_percent:.2f}%")
    print(f"Indexing time: {end_time - start_time:.2f} seconds")
    assert cpu_percent < 85, "CPU usage is too high."

def test_memory_usage():
    document = "Alaska is the largest U.S. state by area." * 10000
    process = psutil.Process()
    memory_before = process.memory_info().rss
    build_index(document)
    memory_after = process.memory_info().rss
    print(f"Memory usage during indexing: {memory_after - memory_before} bytes")
    assert (memory_after - memory_before) < 200 * 1024 * 1024, "Memory usage exceeded limit."
