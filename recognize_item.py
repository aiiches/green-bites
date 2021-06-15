import numpy as np
import pandas as pd
import os
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

cwd = os.getcwd()
df = pd.read_csv(os.path.join(cwd, 'merged_dataset_large.csv'))
known_embeddings = df['Word Embedding'].apply(lambda x:
                           np.fromstring(
                               x.replace('\n','')
                                .replace('[','')
                                .replace(']','')
                                .replace('  ',' '), sep=' '))
known_embeddings = known_embeddings.tolist()
known_embeddings = np.array(known_embeddings)
print(known_embeddings)

wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')


def recognize_item(item_name, known_embeddings):
    embedding = np.zeros(100)
    for i, word in enumerate(item_name.split()):
        embedding = np.add(embedding, wv[word])
    embedding = embedding / (i + 1)
    similarities = cosine_similarity([embedding], known_embeddings)
    max_index = np.argmax(similarities)
    return max_index


print("Welcome to Green Bites!")
print("Enter 'Q' to exit")
user_item = input("Enter any grocery item: ")
while user_item != "Q":
    try:
        index = recognize_item(user_item, known_embeddings)
        print(f"{user_item} is estimated to have a footprint of about {df.loc[index]['Footprint']} kg of CO2 per kg.")
    except:
        print("Sorry, we couldn't recognize that food item. Try another!")
    finally:
        user_item = input("Enter another item: ")

print("Happy shopping!")
