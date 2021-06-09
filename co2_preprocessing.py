
import numpy as np
import pandas as pd
import os
import re

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'data\\ds1_food_footprints.xlsx')
df = pd.read_excel(data_path)

# drop unwanted columns
df = df.drop(['Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23'], axis=1)

# clean labels (remove tags)
df['Item'] = df['Item'].str.replace(r'\*', '')

# Replace 'FOOD (F)' with 'FROZEN FOOD'
# for index, row in df.iterrows():
#     if re.match(r".+ \(F\)", row['Item']):  # if the item is in format "FOOD (F)"
#         food_name = row['Item'].replace(r'\(F\)', '')
#         df.loc[index].at["Item"] = f'FROZEN {food_name}'

df['Item'] = df['Item'].str.replace(r'\(F\)', 'FROZEN')
df['Item'] = df['Item'].str.replace(r'\(.\)', '')
df['Item'] = df['Item'].str.strip()

# create simplified dataframe
df2 = [df['Item'], df['mean']]
headers = ['Item', 'footprint']
df2 = pd.concat(df2, axis=1, keys=headers)

# write to csv
df.to_csv('co2_data.csv')
df2.to_csv('co2_data_simple.csv', index=False)
