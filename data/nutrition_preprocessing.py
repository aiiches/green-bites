
import pandas as pd
import os
from itertools import chain
from gensim.models import Word2Vec

# load food footprints data from excel
cwd = os.getcwd()
parent = os.path.abspath(os.path.join(cwd, os.pardir))
df = pd.read_excel(os.path.join(cwd, 'nutrition\\nutrition_data_raw.xlsx'))
model_path = os.path.join(parent, 'saved_models\\word2vec.model')
model = Word2Vec.load(model_path)

# Remove non descriptive categories
df['Descrip'] = df['Descrip'].str.replace('Alcoholic beverage,', '')
df['Descrip'] = df['Descrip'].str.replace('table,', '')

# separate first row
df[['Type', 'Name', 'Others']] = df.Descrip.str.split(",", n=2, expand=True)

# drop unwanted columns
df = df.drop(['ShortDescrip', 'Descrip', 'Others', 'ID', 'MfgName', 'ScientificName', 'VitA_USRDA', 'VitB6_USRDA',
              'VitB12_USRDA', 'VitC_USRDA', 'VitE_USRDA', 'Folate_USRDA', 'Niacin_USRDA', 'Riboflavin_USRDA',
              'Thiamin_USRDA', 'Calcium_USRDA', 'Copper_USRDA', 'Magnesium_USRDA', 'Phosphorus_USRDA',
              'Selenium_USRDA', 'Zinc_USRDA'], axis=1)

# averaging similar rows
df = df.groupby(['FoodGroup', 'Type', 'Name'], as_index=False).mean()

# Get "Full Name" and format
df.insert(0, 'FullName', df['Type'] + df['Name'])
df['FullName'] = df['FullName'].str.lower()
df['FullName'] = df['FullName'].str.replace('(', '')
df['FullName'] = df['FullName'].str.replace(')', '')
df['FullName'] = df['FullName'].str.replace('&', 'and')
df['FullName'] = df['FullName'].str.replace('/', ' ')
df['FullName'] = df['FullName'].str.replace('-', ' ')
df['FullName'] = df['FullName'].str.strip()

# Drop more unwanted columns
df = df.drop(['FoodGroup', 'Type', 'Name'], axis=1)
df = df.groupby(['FullName'], as_index=False).mean()

# recipes_df = pd.read_csv(os.path.join(cwd, 'recipes\\embeddings.csv'), index_col=0)
# recipe_words = set(recipes_df.index.values)
recipe_words = model.wv.key_to_index
recipe_words = set(recipe_words.keys())

# format nutrient word data (uses type and name)
nutrient_words = df['FullName'].to_list()
for i, item in enumerate(nutrient_words):
    nutrient_words[i] = item.split()
nutrient_words = list(chain.from_iterable(nutrient_words))
nutrient_words = set(nutrient_words)

nutrients_difference = nutrient_words.difference(recipe_words)
nutrients_percent = int((len(nutrients_difference) / len(nutrient_words)) * 100)
print(f'Excluded nutrient words: {nutrients_difference}')
print(f'{len(nutrients_difference)} words from the nutrient dataset (about {nutrients_percent}%) '
      f'are not included in the recipes')

rows_to_drop = []
for i, name in enumerate(df['FullName'].to_list()):
    for word in name.split():
        print(word)
        if word in nutrients_difference:  # name contains a word that is not in the recipe dataset
            rows_to_drop.append(i)
            break
print(len(rows_to_drop))
df = df.drop(rows_to_drop)

# write to csv
df.to_csv('nutrition\\nutrition_data.csv', index=False)
