import numpy as np
import pandas as pd
import os

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'carbon-footprint-tracker\\data\\Food_Nutrients_mod.xlsx')
df = pd.read_excel(data_path)

# separate first row
df[['Type', 'Name', 'Others']] = df.Shrt_Desc.str.split(",", n=2, expand=True)

# drop unwanted columns
df = df.drop(['Shrt_Desc', 'Others'], axis=1)

# If the cell is empty, replace by 0
df.fillna(0, inplace=True)

# averaging similar rows
df2 = df.groupby(['Type', 'Name'], as_index=False).mean()

# write to csv
df2.to_csv('Nutrients_data.csv')