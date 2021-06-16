import numpy as np
import pandas as pd
import os
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

# load datasets
cwd = os.getcwd()
parent = os.path.abspath(os.path.join(cwd, os.pardir))
co2_df = pd.read_csv(os.path.join(cwd, 'co2\\co2_data.csv'))
nutrient_df = pd.read_csv(os.path.join(cwd, 'nutrition\\nutrition_data.csv'))

# load trained word2vec model
model_path = os.path.join(parent, 'saved_models\\word2vec.wordvectors')
wv = KeyedVectors.load(model_path, mmap='r')

# Get name embeddings for each label in the nutrition dataset, and include in the dataframe
embeddings_list = []
for index, row in nutrient_df.iterrows():
    vector_sum = np.zeros(100)
    item_name = row['FullName']
    for i, word in enumerate(item_name.split()):  # for each word in the item name
        vector = wv[word]  # find the vector from the embeddings dataset
        vector_sum = np.add(vector_sum, vector)
    embeddings_list.append(vector_sum / (i + 1))
nutrient_df.insert(1, 'Word Embedding', embeddings_list)

# For each name in the co2 dataset, get word embeddings for each word
embeddings_list = []
for index, row in co2_df.iterrows():
    vector_sum = np.zeros(100)
    item_name = row['Item']
    for i, word in enumerate(item_name.split()):  # for each word in the item name
        vector = wv[word]  # find the vector from the embeddings dataset
        vector_sum = np.add(vector_sum, vector)
    embeddings_list.append(vector_sum / (i + 1))
co2_df.insert(1, 'WordEmbedding', embeddings_list)

# Find the best nutrition matches between the two datasets
vector1 = co2_df['WordEmbedding'].tolist()
vector1 = np.array(vector1)

vector2 = nutrient_df['Word Embedding'].tolist()
vector2 = np.array(vector2)

similarities = cosine_similarity(vector1, vector2)
max_1 = np.argmax(similarities, axis=0)  # for each element in the nutrition dataset
max_2 = np.argmax(similarities, axis=1)  # for each element in the co2 dataset

df_tomerge = pd.DataFrame(columns=(nutrient_df.columns))
for i, index in enumerate(max_2):
    df_tomerge.loc[i] = nutrient_df.loc[index]

df_merged = pd.concat([co2_df, df_tomerge], axis=1)
df_merged = df_merged.drop(['WordEmbedding'], axis=1)
df_merged.to_csv('merged_dataset.csv', index=False)

df_tomerge2 = pd.DataFrame(columns=(co2_df.columns))
for i, index in enumerate(max_1):
    df_tomerge2.loc[i] = co2_df.loc[index]

df_merged = pd.concat([nutrient_df, df_tomerge2], axis=1)
df_merged = df_merged.drop(['WordEmbedding'], axis=1)
df_merged.to_csv('merged_dataset_large.csv', index=False)
