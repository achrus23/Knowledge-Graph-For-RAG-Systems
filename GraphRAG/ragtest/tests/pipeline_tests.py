import pytest
from graphrag.index.run.run import run_pipeline, run_pipeline_with_config

class TestGraphRAGPipeline:
    def test_run_pipeline(self):
        """
        Test running the default pipeline.
        """
        try:
            # Simulate a simple pipeline execution
            result = run_pipeline()
            assert result is not None, "Pipeline execution failed."
            print("Pipeline executed successfully:", result)
        except Exception as e:
            pytest.fail(f"Pipeline execution raised an exception: {e}")

    def test_run_pipeline_with_config(self):
        """
        Test running the pipeline with a custom configuration.
        """
        custom_config = {
            "input": "Alaska is the largest U.S. state by area.",
            "mode": "hybrid",
        }
        try:
            # Run pipeline with custom configuration
            result = run_pipeline_with_config(custom_config)
            assert result is not None, "Pipeline execution with config failed."
            assert isinstance(result, dict), "Pipeline result should be a dictionary."
            print("Pipeline executed with config successfully:", result)
        except Exception as e:
            pytest.fail(f"Pipeline execution with config raised an exception: {e}")


if __name__ == "__main__":
    pytest.main()
