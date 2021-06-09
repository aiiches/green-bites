import numpy as np
import pandas as pd
import os

# load food footprints data from excel
cwd = os.getcwd()
data_path = os.path.join(cwd, 'data\\Food_Nutrients.xlsx')
df = pd.read_excel(data_path)

# Change abreviations

df['Shrt_Desc'] = df['Shrt_Desc'].str.replace('ALCOHOLIC BEV,', '')
df['Shrt_Desc'] = df['Shrt_Desc'].str.replace('TABLE,', '')

# separate first row
df[['Type', 'Name', 'Others']] = df.Shrt_Desc.str.split(",", n=2, expand=True)

# drop unwanted columns
df = df.drop(['Shrt_Desc', 'Others', 'NDB_No', 'GmWt_Desc1', 'GmWt_Desc2'], axis=1)
# should we remove others colomns (Those with too many missing values)

# If the cell is empty, replace by 0 (Don't know if its the best way to do it)
df.fillna(0, inplace=True)

# averaging similar rows
df2 = df.groupby(['Type', 'Name'], as_index=False).mean()


# write to csv
df2.to_csv('Nutrients_data.csv')