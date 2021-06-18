import pandas as pd
import os

cwd = os.getcwd()
data_path = os.path.join(cwd, 'data\\GroceryStoreDataset-master\\dataset\\classes.csv')
df = pd.read_csv(data_path)
df2 = df[['Coarse Class ID (int)', 'Coarse Class Name (str)']]

df2 = df2.drop_duplicates()

df2.to_csv('data\\GroceryStoreDataset-master\\dataset\\clean_classes.csv', index=False)
