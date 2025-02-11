# Instructions to setup and run GraphRAG

## Prerequisites

Ensure the following dependencies are installed before starting:
1. **Python**: Version 3.8 or higher.
2. **OpenAI API Key**: We have used the paid version of gpt-4o-mini from OpenAI API to generate the knowledge graph index.

## Install the GraphRAG python library

Run the below command to install the graphrag python library:
```bash
pip install graphrag
```

## Create a GraphRAG project

We'll use the graphrag python library to generate the project skeleton

Run the below command to generate the project directory:
```bash
graphrag init --root ./ragtest
```
This will generate a directory ```ragtest``` at the root folder with the below files and sub-directories:
1. **prompts**
2. **.env**
3. **settings.yaml**

Inside this directory, create a new folder ```input```. This is where we'll add the input text files.

## Modify settings and environment variables

In the ```ragtest/settings.yaml``` we have to add the name of the model we'll be using. In our case, we're using the **gpt-4o-mini** model. We have also enabled **graphml** under the **snapshots**, which simplifies the visualization of the knowledge graph index

```yaml
llm:
  model: gpt-4o-mini
  ...
...
snapshots:
  graphml: true
  ...
...
```

## Build a knowledge graph index

To build a knowledge graph index, we'll have to add some text files in the ```ragtest/input``` directory

Once we have all the files in place, the below command is run:
```bash
graphrag index --root ./ragtest
```
This will generate files in the below directories:
1. **logs**: containing the execution log
2. **output**: containing the parquet files corresponding to the knowledge graph index