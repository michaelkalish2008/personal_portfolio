# Personal Portfolio

Welcome to my GitHub portfolio! You might know me from the Netflix show "You are What You Eat" or as co-winner of Food Network's "Great Food Truck Race" (Series 7) and co-finalists on "Chopped" (Twins for the Win). I have worn a lot of hats, which has given my career in Data Science a special flavor. 

Data science is about posing questions and using data to get context, insight and perspective for making quick and thoughtful decision. This repository showcases my skills as both a data scientist and a problem solver. It's a living document, regularly updated as I develop new skills and complete projects, providing a comprehensive overview of my coding abilities and achievements.

## Introduction

My career intersects data science, trust & safety/compliance, and privacy. I lead and manage end-to-end projects, working with cross-functional teams to tackle local, regional, and global challenges. I graduate from my Masters in Data Science program (MIDS) at UC Berkeley in Spring 2025 and have specialized in NLP/ML. Here are some of the tools I use:

- **SQL**
- **Python**
- **Regex**
- **Graph Data Science**
- **Machine Learning**
- **Natural Language Processing**

## Repository Structure

Below is the structure of this repository, which includes various files and directories associated with my projects:

**personal_portfolio/**
  - **Dockerfile**: Configuration file for Docker, used to build Docker containers. Once you go Docker, it's so hard to go back to running pip and anaconda straight on my computer...just build an image and run containers when you need them! Something goes wrong with the environment? Destroy the container and create a new one. Amazing.
  - **docker-compose.yaml**: A YAML file starting up a new docker container. Just execute "docker-compose up -d' from the directory and you got yourself a working environment for the whole repo!
  - **requirements.txt**: Lists all Python libraries required by the projects within the repo and used to build the docker image I use.
  - **data/**: Raw data files used in projects.
  - **genai/**: Use of LLMs to parse, summarize and reformat unstructured text data pulled from an FDA webpage
  - **classification/**: non-deep learning ML-based classification
  - **ml_from_scratch**: logistic regression and a neural net from scratch for binary classification
  - **pdf_to_table**: pdf data extraction and conversion to a table format
  - **text_to_audio**: A simple conversion of text to audio using gTTS (a transcription package)
  - **webscraping**: Webscraping of a database containing shark attack data for Hawaii
  - **fda_and_usda_apis**: Calls to the FDA and USDA APIs for recall data, which is reformatted into a table

## Contact Me

Interested in collaborating or learning more about my work? Feel free to reach out!

- **Email**: [mtkalish@gmail.com](mtkalish@gmail.com)


