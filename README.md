# Clothing Similarity Search

The Clothing Similarity Search project is a machine learning-based solution that aims to find similar clothing items based on their descriptions. It utilizes natural language processing techniques and web scraping to extract features from clothing item descriptions and rank them based on similarity.

## Project Structure

The project is organized into several modules and files:

- `main.py`: Contains the entry point for the clothing similarity search function.
- `scraper.py`: Implements web scraping functionality to gather clothing item descriptions from websites.
- `cleaner.py`: Provides functions for cleaning and preprocessing text data.
- `feature_extraction.py`: Defines methods for extracting useful features from text descriptions.
- `similarity_calculation.py`: Calculates the similarity between the input text and the clothing item descriptions.
- `ranker.py`: Ranks the clothing items based on similarity scores.
- `cloud_functions.py`: Implements the function to be deployed on Google Cloud Functions.
- `cloud_run.py`: Implements the API endpoint for Google Cloud Run deployment.
- `requirements.txt`: Lists the required Python packages and their versions.

## Getting Started

To run the project locally, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/clothing-similarity-search.git

