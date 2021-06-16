
import pandas as pd
import os
from itertools import chain

# load food footprints data from excel
cwd = os.getcwd()
df = pd.read_excel(os.path.join(cwd, 'co2\\co2_data_raw.xlsx'))
recipes_df = pd.read_csv(os.path.join(cwd, 'recipes\\embeddings.csv'), index_col=0)

# drop unwanted columns
df = df.drop(['Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)

# clean labels (remove tags)
df['Item'] = df['Item'].str.replace(r'\*', '')
df['Item'] = df['Item'].str.replace(r'\(F\)', 'FROZEN')
df['Item'] = df['Item'].str.replace(r'\(.\)', '')

df['Item'] = df['Item'].str.replace('&', 'and')
df['Item'] = df['Item'].str.replace('-', ' ')
df['Item'] = df['Item'].str.strip()
df['Item'] = df['Item'].str.lower()

# create simplified dataframe
df2 = [df['Item'], df['mean']]
headers = ['Item', 'Footprint']
df2 = pd.concat(df2, axis=1, keys=headers)

co2_words = df2['Item'].to_list()
for i, item in enumerate(co2_words):
    co2_words[i] = item.split()
co2_words = list(chain.from_iterable(co2_words))
co2_words = set(co2_words)

recipe_words = set(recipes_df.index.values)

co2_difference = co2_words.difference(recipe_words)
co2_percent = int((len(co2_difference) / len(co2_words)) * 100)
print(f'Excluded co2 words: {co2_difference}')
print(f'{len(co2_difference)} words from the co2 dataset (about {co2_percent}%) are not included in the recipes')

# Filter co2 data
rows_to_drop = []
for i, name in enumerate(df2['Item'].to_list()):
    for word in name.split():
        if word in co2_difference:  # name contains a word from co2_difference
            rows_to_drop.append(i)
            break
df2 = df2.drop(rows_to_drop)

# write to csv
df2.to_csv('co2\\co2_data.csv', index=False)
