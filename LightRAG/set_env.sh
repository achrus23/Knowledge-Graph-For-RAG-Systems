#!/bin/bash

# Set environment variables
export RAG_DIR="index_default"  # Directory for storing the RAG index
export OPENAI_BASE_URL="https://api.openai.com/v1"  # OpenAI API base URL
export OPENAI_API_KEY="your_openai_api_key"  # Replace with your actual OpenAI API key. Not mentioning ours for privacy reasons.
export LLM_MODEL="gpt-4o-mini"  # LLM model
export EMBEDDING_MODEL="text-embedding-3-large"  # Embedding model

# Print the values to verify
echo "RAG_DIR set to: $RAG_DIR"
echo "OPENAI_BASE_URL set to: $OPENAI_BASE_URL"
echo "OPENAI_API_KEY set to: $OPENAI_API_KEY"
echo "LLM_MODEL set to: $LLM_MODEL"
echo "EMBEDDING_MODEL set to: $EMBEDDING_MODEL"
