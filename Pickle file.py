import pickle

# Save the results_df DataFrame to a pickle file
with open('sentiment_results.pkl', 'wb') as file:
    pickle.dump(results_df, file)


# Load the DataFrame from the pickle file
with open('sentiment_results.pkl', 'rb') as file:
    loaded_results_df = pickle.load(file)
