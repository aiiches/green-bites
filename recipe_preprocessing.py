import pandas as pd
import os

cwd = os.getcwd()
recipes_path = os.path.join(cwd, 'data\\recipe_data_raw.xls')
df = pd.read_excel(recipes_path)

df['Recipes'] = df['Recipes'].str.lower()
df['Recipes'] = df['Recipes'].str.replace('(', '')
df['Recipes'] = df['Recipes'].str.replace(')', '')
df['Recipes'] = df['Recipes'].str.replace('&', 'and')
df['Recipes'] = df['Recipes'].str.replace('/', ' ')
df['Recipes'] = df['Recipes'].str.replace('-', ' ')
df['Recipes'] = df['Recipes'].str.replace(',', '')
df['Recipes'] = df['Recipes'].str.replace('\'', '')
df['Recipes'] = df['Recipes'].str.replace('\"', '')
df['Recipes'] = df['Recipes'].str.replace(r'[0-9]+', '')
df['Recipes'] = df['Recipes'].str.replace(r'\s+', ' ')
df['Recipes'] = df['Recipes'].str.strip()

df.to_csv('recipe_data.csv', index=False)
