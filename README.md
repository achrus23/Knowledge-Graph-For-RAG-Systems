# Knowledge-Graph-For-RAG-Systems
This project explores the integration of **knowledge graphs** into the **Retrieval-Augmented Generation (RAG)** framework to enhance retrieval relevance and generative AI efficiency. The project evaluates two implementations:  
- **GraphRAG** (Microsoft Research)  
- **LightRAG** (University of Hong Kong)

## Key Features  
- **Graph-Based Retrieval**: Enhances retrieval-augmented generation by incorporating structured knowledge graphs.  
- **Comparison of Two RAG Systems**: Evaluates **GraphRAG** and **LightRAG** based on efficiency, indexing speed, API calls, and retrieval quality.  
- **Optimized Token & API Usage**: LightRAG reduces API calls by **60%**, improving cost efficiency and processing speed.  
- **Knowledge Graph Construction**: Extracts entities and relationships to create structured knowledge graphs for better contextual understanding.  
- **Performance Benchmarking**: Conducted experiments on multiple datasets, including **literary text, Wikipedia, and fiction**, to analyze retrieval accuracy and efficiency.  
- **Scalability & Real-Time Processing**: Designed for efficient query adaptation, making it suitable for **large-scale** and **real-time applications**.  

## Setup  
For both models, the setup instructions can be found in their respective branches.

### **Prerequisites**  
- Python **3.8+** (GraphRAG) / Python **3.10+** (LightRAG)  
- OpenAI API key for GPT-4o-mini  
- Conda (optional for environment management)  

## Datasets
The datasets used are in .txt formats and they are as follows:
1. 1st Book of Game of Thrones(A Song of Ice and Fire)
2. A Christmas Carol book
3. A set of Wikipedia artilces based on 5 states of USA.

## Results
These are 2 sample knowledge graph results that were generated for each models for the dataset Game of Thrones Book. 

![gotbookop](https://github.com/user-attachments/assets/81ad9bb2-89ff-4602-aef7-4b3831b706d3)

A sample gif showing the various entities and relationships created in a knowledge graph after indexing based on Graphrag.

![Gotbooklightrag](https://github.com/user-attachments/assets/2b6d4c5f-488e-48a5-a38a-263c5a0b17de)

A sample gif showing the various entities and relationships created in a knowledge graph  after indexing based on lightrag.

## Observations  
- **GraphRAG captures more relationships but at a higher cost**: It created **278% more relationships** compared to LightRAG, leading to richer contextual responses but requiring more processing time and API requests.  
- **LightRAG is faster and more cost-efficient**: It reduced API requests by **60%** and indexing time by **32%**, making it suitable for real-time applications.  
- **GraphRAG excels in deep contextual understanding**: It generated **more detailed responses**, useful for applications requiring complex knowledge representation.  
- **LightRAG prioritizes efficiency**: It optimized token handling and reduced computational overhead, making it a practical choice for resource-constrained environments.  
- **Trade-off between detail and speed**: While GraphRAG provides **richer insights**, LightRAG delivers **faster and more scalable** results, depending on application needs.

## Challenges and Solutions  

### Challenges  
- **High API Overhead in GraphRAG**: The system required significantly more API requests, increasing operational costs and slowing down retrieval.  
- **Token-Intensive Processing**: Managing large datasets led to excessive token usage, impacting efficiency and scalability.  
- **Complex Knowledge Graphs Slowed Queries**: The dense structure of GraphRAG’s knowledge graph made query processing slower and harder to interpret.  

### Solutions  
- **Optimized API Calls and Query Aggregation**: Implemented caching and batch processing, reducing API requests by **70%**, cutting costs, and improving response times.  
- **Token Pruning and Prioritization**: Introduced efficient token usage techniques to process large datasets without increasing costs or slowing down retrieval.  
- **Hierarchical Graph Structures for Faster Retrieval**: Simplified graph representations to improve query speed and enhance system interpretability.  

