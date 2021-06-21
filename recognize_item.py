import numpy as np
import pandas as pd
import os
from gensim.models import KeyedVectors
from sklearn.metrics.pairwise import cosine_similarity

cwd = os.getcwd()
df = pd.read_csv(os.path.join(cwd, 'data/merged_dataset.csv'))
known_embeddings = df['Word Embedding'].apply(lambda x:
                           np.fromstring(
                               x.replace('\n','')
                                .replace('[','')
                                .replace(']','')
                                .replace('  ',' '), sep=' '))
known_embeddings = known_embeddings.tolist()
known_embeddings = np.array(known_embeddings)

model_path = os.path.join(cwd, 'saved_models/word2vec.wordvectors')
wv = KeyedVectors.load(model_path, mmap='r')


def recognize_item(item_name):
    """
          recognizes the user input and finds the closest match in the full dataset
          :param emb: list of embeddings in the full dataset (implicit from outer scope)
          :param item_name: item entered by the user (string)
          :return: dataframe row containing the item that is the best match from the dataset
    """
    item_name = item_name.lower()
    embedding = np.zeros(100)
    for i, word in enumerate(item_name.split()):
        embedding = np.add(embedding, wv[word])
    embedding = embedding / (i + 1)
    similarities = cosine_similarity([embedding], known_embeddings)
    max_index = np.argmax(similarities)
    return df.loc[max_index]


if __name__ == '__main__':
    print("Welcome to Green Bites!")
    print("Enter 'Q' to exit")
    user_item = input("Enter any grocery item: ")
    user_item = user_item.lower()
    while user_item != "Q":
        try:
            item = recognize_item(user_item)
            print(f"{user_item} is estimated to have a footprint of about {item['Footprint']} kg of CO2 per kg.")
        except:
            print("Sorry, we couldn't recognize that food item. Try another!")
        finally:
            user_item = input("Enter another item: ")

    print("Happy shopping!")
