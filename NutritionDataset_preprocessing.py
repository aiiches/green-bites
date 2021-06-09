import numpy as np
import pandas as pd
import os

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'data\\nutritionnalvalues.xlsx')
df = pd.read_excel(data_path)

# Remove non descriptive categories
df['Descrip'] = df['Descrip'].str.replace('Alcoholic beverage,', '')
df['Descrip'] = df['Descrip'].str.replace('table,', '')

# separate first row
df[['Type', 'Name', 'Others']] = df.Descrip.str.split(",", n=2, expand=True)

# drop unwanted columns
df = df.drop(['ShortDescrip', 'Descrip', 'Others', 'ID', 'MfgName', 'ScientificName'], axis=1)

# averaging similar rows
df2 = df.groupby(['FoodGroup','Type', 'Name'], as_index=False).mean()


# write to csv

df2.to_csv('Nutrients_data.csv')