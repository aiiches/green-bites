import numpy as np
import pandas as pd
import os

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'nutrition\\nutrition_data_raw.xlsx')
df = pd.read_excel(data_path)

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

# write to csv
df.to_csv('nutrition\\nutrition_data.csv', index=False)
