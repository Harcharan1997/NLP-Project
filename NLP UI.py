import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from tqdm.notebook import tqdm
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
from scipy.special import softmax
import tensorflow as tf
from transformers import pipeline
import tkinter as tk
from tkinter import scrolledtext

# Initialize the necessary variables
sia = SentimentIntensityAnalyzer()
MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = TFAutoModelForSequenceClassification.from_pretrained(MODEL)


# Function to perform sentiment analysis using RoBERTa
def polarity_scores_roberta(example):
    # Encode text using the tokenizer with padding and truncation
    encoded_text = tokenizer(example, return_tensors='tf', padding='max_length', truncation=True, max_length=512)

    # Convert the TensorFlow tensors
    input_ids = encoded_text['input_ids']
    attention_mask = encoded_text['attention_mask']

    # Pass tensors to the model
    output = model(input_ids=input_ids, attention_mask=attention_mask)

    scores = output.logits[0].numpy()
    scores = tf.nn.softmax(scores, axis=-1).numpy()

    scores_dict = {
        'roberta_neg': scores[0],
        'roberta_neu': scores[1],
        'roberta_pos': scores[2]
    }

    return scores_dict

# Function to update the GUI with results
example = "This is an example text for sentiment analysis."

def update_results_text():
    results_text.delete(1.0, tk.END)  # Clear previous results
    results_text.insert(tk.END, "Results:\n\n")
    

    
    # Display results in the text widget
    results_text.insert(tk.END, "Example Result:\n")
    results_text.insert(tk.END, f"{example}\n")
    results_text.insert(tk.END, f"VADER Scores: {sia.polarity_scores(example)}\n")
    results_text.insert(tk.END, f"RoBERTa Scores: {polarity_scores_roberta(example)}\n\n")
    
    # Add more results as needed...

# Function to handle button click event
def analyze_button_clicked():
    update_results_text()

# Create main window
window = tk.Tk()
window.title("Sentiment Analysis App")

# Create and place widgets
analyze_button = tk.Button(window, text="Analyze Sentiment", command=analyze_button_clicked)
analyze_button.pack(pady=10)

results_text = scrolledtext.ScrolledText(window, width=80, height=20)
results_text.pack()

# Run the GUI
window.mainloop()
