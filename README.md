# Interactive Workday Assisstant
## Overview
 
The Interactive Workday Assistant is an internal AI tool that uses Retrieval-Augmented Generation (RAG) combined with a Small Language Model (SLM) to answer HR-related queries securely and contextually. It is designed to help employees retrieve relevant information from Workday without relying on external AI services that could raise data privacy or compliance concerns.
## Why RAG + SLM?
 
- **Small Language Models (SLMs)** are used because the system has a narrow, well-defined scope, making lightweight models more efficient than large general-purpose ones.
- **RAG techniques** enable real-time retrieval of relevant and up-to-date information from internal data sources, without retraining the model.
- **Private sector fit:** RAG-based pipelines can be tailored to match the specific needs of an organization rather than serving general use cases.

## To run this program
First build a docker image with the command:\
docker build -t group-project-image .\
Then create a docker container with the command:\
docker run -d -p 3306:3306 --name group-project group-project-image\
Once the container is created, open a shell inside the container with the command:\
docker exec -it group-project bash

## Dataset
 
Data is sourced from the Workday Worker API and converted to a JSON format. For demonstration purposes, a synthetic dataset mirroring the structure of real Workday API responses was used.
 
The types of data queried include:
- Personal information
- Job details
- Employment information
- Contact information


### To run the testing script, use the following:
./tester.sh


### To run the program, use the following command:
python3 RAG.py


Once that is done, you will be prompted to enter a query. Enter your query and wait until the
LLM generates a response. Then, you will be prompted to enter a new query or exit system.

Note: The build takes lot of time, because of the amount of libraries and code files that are imported
Be prepared for the code to take 25+ minutes to build, depending on system configuration.
