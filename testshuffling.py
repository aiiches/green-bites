from sklearn.utils import shuffle
import os
import pandas as pd
import numpy as np


def shuffling():
    cwd = os.getcwd()
    train_csv_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/train.txt')
    df = pd.read_csv(train_csv_path, delimiter = ',', names=["path", "precision", "name"])
    df = shuffle(df)
    df.to_csv(r'data/GroceryStoreDataset-master/dataset/shuffledtrain.txt', header=None, index=None, sep=',', mode='a')

