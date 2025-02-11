import random
import string
from graphrag.api.index import build_index
import time

def generate_large_document(size_in_mb):
    """Generate a random document of a given size (in MB)."""
    size = size_in_mb * 1024 * 1024  # Convert to bytes
    return ''.join(random.choices(string.ascii_letters + " ", k=size))

def test_scalability():
    sizes = [1, 10, 50, 100]  # Dataset sizes in MB
    for size in sizes:
        document = generate_large_document(size)
        start_time = time.time()
        build_index(document)
        end_time = time.time()
        print(f"Indexing time for {size} MB: {end_time - start_time:.2f} seconds")
        assert end_time - start_time < size * 0.5, f"Indexing for {size} MB took too long."
