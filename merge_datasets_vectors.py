import numpy as np
import pandas as pd
import os

# load trained word2vec model

cwd = os.getcwd()
emb_df = pd.read_csv(os.path.join(cwd, 'embeddings.csv'), index_col=0)
co2_df = pd.read_csv(os.path.join(cwd, 'co2_data_filtered.csv'))
nutrient_df = pd.read_csv(os.path.join(cwd, 'nutrition_data_filtered.csv'))

print(emb_df)
# Get name embeddings for each label in the nutrition dataset, and include in the dataframe
embeddings_list = []
vector_sum = np.zeros(100)
item_name = nutrient_df['FullName'].to_list()[0]
for word in item_name.split():  # for each word in the item name
    vector = emb_df.loc[word]  # find the vector from the embeddings dataset
    vector = vector.to_numpy()
    print(f'{word}: {vector}')
    vector_sum = np.add(vector_sum, vector)
print(vector_sum)

# For each name in the nutrition dataset, get word embeddings for each word


# Add the vectors together to get the embedding for the full name


# Add this to the dataframe


# Find the best nutrition match for each word in the co2 dataset


# For a single co2 entry, find word embeddings for each word in the co2 dataset


# Add the vectors together to get the embedding for the full name


# Calculate the cosine similarity with each element of the nutrition dataset


# Pick the nutrition element that has the largest similarity


# Append the nutrition data to the co2 entry
