#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install -U gensim


# In[3]:


pip install --upgrade gensim


# In[2]:


pip install numpy --upgrade


# In[2]:


pip install python-Levenshtein


# In[8]:


pip install s3fs


# In[1]:


import boto3
import pandas as pd
from sagemaker import get_execution_role

role = get_execution_role()
bucket='montreal-team5'
data_key = 'recipes.csv'
data_location = 's3://montreal-team5/recipes.csv'.format(bucket, data_key)

pd.read_csv(data_location)


# In[4]:


import os
import csv
import spacy
import pandas as pd
import gensim
from pprint import pprint as pp

class Corpus(object):

    def __init__(self, filename):
        self.filename = filename
        self.nlp = spacy.blank("en")
        
    def __iter__(self):
        with open(self.filename, "r") as i:
            reader = csv.reader(i, delimiter=",")
            for abstract in reader:
                tokens = [t.text.lower() for t in self.nlp(abstract[0]) if t.text.lower().isalnum()]
                yield tokens

documents = Corpus("./recipes.csv")

model = gensim.models.Word2Vec(sentences=documents, vector_size=100)
dictionary = model.wv.key_to_index
# pp(dictionary)
similar_words = model.wv.similar_by_word("soup", topn=10)
pp(similar_words)

# model.wv.most_similar(positive=["tree"], negative=["during"], topn=10)
# In[6]:


model.save("word2vec.model")


# In[1]:


import pickle

loaded_model = pickle.load(open("word2vec.model", 'rb'))


# In[3]:


from gensim.models import KeyedVectors

# Store just the words + their trained embeddings.
word_vectors = loaded_model.wv
word_vectors.save("word2vec.wordvectors")

# Load back with memory-mapping = read-only, shared across processes.
wv = KeyedVectors.load("word2vec.wordvectors", mmap='r')
vector = wv['potato']  # Get numpy vector of a word

pp(vector)


# In[5]:


from pprint import pprint as pp
vector2 = wv['squash']  # Get numpy vector of a word
pp (vector2)


# In[15]:



# In[ ]:




