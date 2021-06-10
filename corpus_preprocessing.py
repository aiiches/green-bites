
import numpy as np
import pandas as pd
import os
from itertools import chain
import re

pattern = re.compile('[\W_0-9]+')

# load data from excel files
cwd = os.getcwd()
co2_path = os.path.join(cwd, 'co2_data_simple.csv')
nutrients_path = os.path.join(cwd, 'Nutrients_data.csv')
recipes_path = os.path.join(cwd, 'data\\recipes.xls')

# crate dataframes
co2_df = pd.read_csv(co2_path)
nutrient_df = pd.read_csv(nutrients_path)
recipes_df = pd.read_excel(recipes_path)

# format co2 word data
co2_words = co2_df['Item'].to_list()
for i, item in enumerate(co2_words):
    item = item.lower()
    item = item.split()
    for j, word in enumerate(item):
        item[j] = pattern.sub(' ', word)
    co2_words[i] = item
co2_words = list(chain.from_iterable(co2_words))
co2_words = set(co2_words)

# format nutrient word data (uses type and name)
nutrient_words = nutrient_df['Type'].to_list() + nutrient_df['Name'].to_list()
for i, item in enumerate(nutrient_words):
    item = item.lower()
    item = item.split()
    for j, word in enumerate(item):
        item[j] = pattern.sub(' ', word)
    nutrient_words[i] = item
nutrient_words = list(chain.from_iterable(nutrient_words))
nutrient_words = set(nutrient_words)

# format recipe word data
recipe_words = recipes_df['Recipes'].to_list()
for i, item in enumerate(recipe_words):
    item = item.split()
    for j, word in enumerate(item):
        word = word.lower()
        word = pattern.sub(' ', word)
        item[j] = word
    recipe_words[i] = item
recipe_words = list(chain.from_iterable(recipe_words))
recipe_words = set(recipe_words)

# find excluded words
co2_difference = co2_words.difference(recipe_words)
co2_percent = int((len(co2_difference) / len(co2_words)) * 100)
nutrients_difference = nutrient_words.difference(recipe_words)
nutrients_percent = int((len(nutrients_difference) / len(nutrient_words)) * 100)

print(f'Excluded co2 words: {co2_difference}')
print(f'{len(co2_difference)} words from the co2 dataset (about {co2_percent}%) are not included in the recipes')

print(f'Excluded nutrient words: {nutrients_difference}')
print(f'{len(nutrients_difference)} words from the co2 dataset (about {nutrients_percent}%) are not included in the recipes')
