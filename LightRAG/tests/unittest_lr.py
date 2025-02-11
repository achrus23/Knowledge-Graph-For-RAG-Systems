import unittest
import os
import shutil
import json
from lightrag import LightRAG, QueryParam
from lightrag.llm import gpt_4o_mini_complete
import logging

# Define constants for the LightRAG setup
WORKING_DIR = "./testing_lr"
gpt_4o_mini_complete = lambda x: x  # Replace with the actual LLM model function


class TestLightRAG(unittest.IsolatedAsyncioTestCase):
    # """Test suite for LightRAG functionality."""

    async def asyncSetUp(self):
    # """Set up LightRAG system with the dataset."""
    # Ensure logging handlers are closed
    import logging
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
        handler.close()

    with open('001ssb.txt', 'r', encoding="utf-8") as f:
        self.dataset = f.read()

    # Initialize LightRAG with working directory and async LLM function
    self.light_rag = LightRAG(
        working_dir=WORKING_DIR,
        llm_model_func=gpt_4o_mini_complete
    )

    # Clean the working directory
    if os.path.exists(WORKING_DIR):
        for filename in os.listdir(WORKING_DIR):
            file_path = os.path.join(WORKING_DIR, filename)
            try:
                os.unlink(file_path)
            except PermissionError:
                print(f"Skipping file in use: {file_path}")
    else:
        os.makedirs(WORKING_DIR)

    # Insert the dataset into the LightRAG system
    await self.light_rag.insert(self.dataset)

async def tearDown(self):
    """Cleanup the working directory after each test."""
    if os.path.exists(WORKING_DIR):
        for filename in os.listdir(WORKING_DIR):
            file_path = os.path.join(WORKING_DIR, filename)
            try:
                os.unlink(file_path)
            except PermissionError:
                print(f"Skipping file in use: {file_path}")


    async def test_retrieval(self):
        """Test if LightRAG retrieves relevant information."""
        query = "Who are the members of the Night's Watch?"
        results = await self.light_rag.retrieve(query)
        self.assertTrue(any("Gared" in result for result in results))
        self.assertTrue(any("Ser Waymar Royce" in result for result in results))

    async def test_generation(self):
        """Test text generation in LightRAG."""
        query = "Describe Ser Waymar Royce's attire."
        response = await self.light_rag.generate(query)
        self.assertIn("Response to:", response["text"])  # Adjust based on actual LLM output

    def test_file_creation(self):
        """Test if the required files are created after insertion."""
        expected_files = [
            "vdb_chunks.json",
            "vdb_entities.json",
            "vdb_relationships.json"
        ]
        for filename in expected_files:
            file_path = os.path.join(WORKING_DIR, filename)
            self.assertTrue(os.path.isfile(file_path), f"{filename} was not created.")

    def test_file_content(self):
        """Test the content of created files to ensure they contain valid JSON."""
        expected_files = [
            "vdb_chunks.json",
            "vdb_entities.json",
            "vdb_relationships.json"
        ]
        for filename in expected_files:
            file_path = os.path.join(WORKING_DIR, filename)
            with open(file_path, 'r', encoding="utf-8") as f:
                try:
                    content = json.load(f)
                    self.assertIsInstance(content, dict, f"{filename} does not contain a valid JSON object.")
                except json.JSONDecodeError:
                    self.fail(f"{filename} contains invalid JSON.")

    async def test_query_naive_mode(self):
        """Test query with mode 'naive'."""
        query = "What are the top themes in this story?"
        response = await self.light_rag.query(query, param=QueryParam(mode="naive"))
        self.assertIsInstance(response, list, "Response should be a list of strings.")
        self.assertGreater(len(response), 0, "Response should not be empty.")

    async def test_query_local_mode(self):
        """Test query with mode 'local'."""
        query = "What are the top themes in this story?"
        response = await self.light_rag.query(query, param=QueryParam(mode="local"))
        self.assertIsInstance(response, list, "Response should be a list of strings.")
        self.assertGreater(len(response), 0, "Response should not be empty.")

    async def test_query_global_mode(self):
        """Test query with mode 'global'."""
        query = "What are the top themes in this story?"
        response = await self.light_rag.query(query, param=QueryParam(mode="global"))
        self.assertIsInstance(response, list, "Response should be a list of strings.")
        self.assertGreater(len(response), 0, "Response should not be empty.")

    async def test_query_hybrid_mode(self):
        """Test query with mode 'hybrid'."""
        query = "What are the top themes in this story?"
        response = await self.light_rag.query(query, param=QueryParam(mode="hybrid"))
        self.assertIsInstance(response, list, "Response should be a list of strings.")
        self.assertGreater(len(response), 0, "Response should not be empty.")


if __name__ == '__main__':
    unittest.main()
