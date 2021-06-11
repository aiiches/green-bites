import pandas as pd
import os
from itertools import chain

# load data from excel files
cwd = os.getcwd()
co2_df = pd.read_csv(os.path.join(cwd, 'co2_data.csv'))
nutrient_df = pd.read_csv(os.path.join(cwd, 'nutrition_data.csv'))
recipes_df = pd.read_csv(os.path.join(cwd, 'recipe_data.csv'))

# format co2 word data
co2_words = co2_df['Item'].to_list()
for i, item in enumerate(co2_words):
    co2_words[i] = item.split()
co2_words = list(chain.from_iterable(co2_words))
co2_words = set(co2_words)
print(co2_words)

# format nutrient word data (uses type and name)
nutrient_words = nutrient_df['FullName'].to_list()
for i, item in enumerate(nutrient_words):
    nutrient_words[i] = item.split()
nutrient_words = list(chain.from_iterable(nutrient_words))
nutrient_words = set(nutrient_words)
print(nutrient_words)

# format recipe word data
recipe_words = recipes_df['Recipes'].to_list()
for i, item in enumerate(recipe_words):
    recipe_words[i] = item.split()
recipe_words = list(chain.from_iterable(recipe_words))
recipe_words = set(recipe_words)
print(recipe_words)

# find excluded words
co2_difference = co2_words.difference(recipe_words)
co2_percent = int((len(co2_difference) / len(co2_words)) * 100)
nutrients_difference = nutrient_words.difference(recipe_words)
nutrients_percent = int((len(nutrients_difference) / len(nutrient_words)) * 100)

print(f'Excluded co2 words: {co2_difference}')
print(f'{len(co2_difference)} words from the co2 dataset (about {co2_percent}%) are not included in the recipes')

print(f'Excluded nutrient words: {nutrients_difference}')
print(f'{len(nutrients_difference)} words from the nutrient dataset (about {nutrients_percent}%) '
      f'are not included in the recipes')

# Filter co2 data
rows_to_drop = []
for i, name in enumerate(co2_df['Item'].to_list()):
    for word in co2_difference:
        if name.find(word) != -1:  # name contains a word from co2_difference
            rows_to_drop.append(i)
            break
co2_df = co2_df.drop(rows_to_drop)
co2_df.to_csv('co2_data_filtered.csv', index=False)

# filter nutrient data
rows_to_drop = []
for i, name in enumerate(nutrient_df['FullName'].to_list()):
    for word in nutrients_difference:
        if name.find(word) != -1:  # name contains a word from co2_difference
            rows_to_drop.append(i)
            break
nutrient_df = nutrient_df.drop(rows_to_drop)
nutrient_df.to_csv('nutrient_data_filtered.csv', index=False)
