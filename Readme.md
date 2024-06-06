This repository contains the codes for the following  weaviate projects: 
1. CODEGEN-RAG: A full stack RAG project for generating python codes and explanations using vector search and generative search.
  
2. LinkedIN ML/AI jobs : The analytics pipeline

3. CODEGEN_Weaviate_workflow.ipynb: The Weaviate workflow for CODEGEN that involves processing of the dataset and populating the Weaviate database.


In detail:
1. CODEGEN-RAG
   
The project works using vector search for python codes and by generating explanations and pseudocodes for the codes produced by the vector search.


The vector search is done by initially populating the weaviate vector database runing on a sandbox instance on Weaviate Cloud (WCD) [https://weaviate.io/developers/weaviate/quickstart] with modulated data from the flytech/python-codes-25k database [https://huggingface.co/datasets/flytech/python-codes-25k]


For the RAG implementation, Cohere based Generative Search module is used [https://weaviate.io/developers/weaviate/modules/reader-generator-modules/generative-cohere]


The project includes backend and frontend folders. The backend relies on python and django rest framework. The frontend is based on Reactjs, tailwindCSS and axios as the mediator between the frontend and backend parts. In addition, prismjs is used for syntax highlighting python code outputs in the webpage.

![screen-1](CODEGEN_search_page.png)

![screen-2](CODEGEN_search_page-2.png)

Flow diagram for CODEGEN:

![flowchart](flowchart.png)