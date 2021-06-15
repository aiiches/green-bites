import pandas as pd
import os

# load trained word2vec model
cwd = os.getcwd()
df = pd.read_csv(os.path.join(cwd, 'embeddings.csv'), index_col=0)
print(df)

# Get name embeddings for each label in the nutrition dataset, and include in the dataframe


# For each name in the nutrition dataset, get word embeddings for each word


# Add the vectors together to get the embedding for the full name


# Add this to the dataframe


# Find the best nutrition match for each word in the co2 dataset


# For a single co2 entry, find word embeddings for each word in the co2 dataset


# Add the vectors together to get the embedding for the full name


# Calculate the cosine similarity with each element of the nutrition dataset


# Pick the nutrition element that has the largest similarity


# Append the nutrition data to the co2 entry
