# Sentiment-Analysis-Dataset-Analysis

## Overview
This repository contains code and data for exploring and analyzing a sentiment analysis dataset using natural language processing techniques. The dataset comprises Amazon product reviews, and the analysis involves sentiment analysis using two different approaches: VADER sentiment analysis and a pre-trained transformer-based model.

## Contents
- `Reviews.csv`: Raw dataset file containing Amazon product reviews.
- `Sentiment_Analysis.ipynb`: Jupyter Notebook file containing the Python code for sentiment analysis and exploration.
- `README.md`: This README file explaining the contents and purpose of the repository.

## Analysis
The primary objective of this analysis is to understand the sentiment of Amazon product reviews using both VADER sentiment analysis and a transformer-based model. The analysis includes:

- **Data Loading and Overview**: Read the dataset, display basic information (shape, columns, data types), and check for missing values.
- **VADER Sentiment Analysis**: Use the VADER sentiment analysis tool to calculate sentiment scores (negative, neutral, positive, compound) for each review.
- **Transformer-Based Model**: Utilize a pre-trained transformer-based model for sentiment analysis and compare the results with VADER.
- **Exploratory Data Analysis (EDA)**: Explore the distribution of sentiment scores and visualize the relationship between different sentiment aspects.
- **Visualization**: Create visualizations to showcase the sentiment distribution and patterns in the dataset.

## Usage
- **Environment Setup**: Ensure Python and necessary libraries (Pandas, NumPy, Matplotlib, Seaborn, NLTK, Transformers) are installed.
- **Data Import**: Load the dataset using Pandas from the provided 'Reviews.csv' file.
- **Code Execution**: Run the 'Sentiment_Analysis.ipynb' Jupyter Notebook or Python script to execute the analysis step-by-step.
- **Understanding the Code**: Comments and markdown cells within the notebook explain each step and its purpose.
- **Modification and Extension**: Modify the code for additional analysis or customization as needed.

## Requirements
- **Python (3.x)**
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, NLTK, Transformers

## Sentiment Analysis Results
The analysis involves two sentiment analysis methods: VADER sentiment analysis and a transformer-based model. Here are some key findings:

### VADER Sentiment Analysis
- Compound scores range from -1 (most negative) to 1 (most positive).
- Positive reviews tend to have higher compound scores, while negative reviews have lower compound scores.

### Transformer-Based Model
- Utilized a pre-trained transformer-based model for sentiment analysis.
- The model provides sentiment labels (positive, negative) along with confidence scores.

### Visualization
- Visualized the distribution of sentiment scores from both VADER and the transformer-based model.
- Explored patterns and relationships between sentiment aspects.

Feel free to contribute, modify, or use this codebase for your projects!
