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
  - **README.md**: You are reading me right now 😀
  - **src/**: Source code directory containing project-specific subdirectories.
    - **data/**: Raw data files used in projects.
    - **notebooks/**: The purpose of these notebooks is to demonstrate fundamental python and DS skills.
      - **a_b_test.ipynb**: Notebook detailing A/B testing procedures.
      - **api_request.ipynb**: How to use FDA's API for pulling recall data.
      - **lr_from_scratch**: Notebook demonstrating how to build a logistic regression model from scratch - great for anyone revisiting the basics of forward pass and backpropagation.
      - **nn_from_scratch**: Explains the construction of a neural network from the ground up (be sure to review lr_from_scratch first and use to compare)
      - **tfidf_from_scratch**: Illustrates how to implement TF-IDF from scratch in Python (just reminds you how lucky we are to have sklearn's tfidf_vectorizer, which I threw in at the end)


## Contact Me

Interested in collaborating or learning more about my work? Feel free to reach out!

- **Email**: [michael.kalish@berkeley.edu](mailto:michael.kalish@berkeley.edu)


