
import pandas as pd
import os

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'co2\\co2_data_raw.xlsx')
df = pd.read_excel(data_path)

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

# write to csv
df2.to_csv('co2\\co2_data.csv', index=False)
