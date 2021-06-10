
import numpy as np
import pandas as pd
import os
from itertools import chain
import re

# load data from excel files
cwd = os.getcwd()
co2_path = os.path.join(cwd, 'co2_data_simple.csv')
recipes_path = os.path.join(cwd, 'data\\recipes.xls')

# crate dataframes
co2_df = pd.read_csv(co2_path)
recipes_df = pd.read_excel(recipes_path)

# format co2 word data
co2_words = co2_df['Item'].to_list()
for i, item in enumerate(co2_words):
    item = item.lower()
    co2_words[i] = item.split()
co2_words = list(chain.from_iterable(co2_words))
co2_words = set(co2_words)

# format recipe word data
recipe_words = recipes_df['Recipes'].to_list()
pattern = re.compile('[\W_0-9]+')
for i, item in enumerate(recipe_words):
    item = item.split()
    for j, word in enumerate(item):
        word = word.lower()
        word = pattern.sub('', word)
        item[j] = word
    recipe_words[i] = item
recipe_words = list(chain.from_iterable(recipe_words))
recipe_words = set(recipe_words)

# find overlap
overlap = co2_words.intersection(recipe_words)
difference = co2_words.difference(recipe_words)
percent_excluded = int((len(difference) / len(co2_words)) * 100)
print(f'{len(difference)} words from the co2 dataset (about {percent_excluded}%) are not included in the recipes')
