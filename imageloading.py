import os
from torchvision import transforms
import pandas as pd
from PIL import Image
import pickle

# load food item images dataset
cwd = os.getcwd()
data_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/train.txt')
data_path2 = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/test.txt')
df = pd.read_csv(data_path, delimiter = ',', names=["path", "precision", "name"])
df2 = pd.read_csv(data_path2, delimiter = ',', names=["path", "precision", "name"])

img_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/')

train_x = []
train_y = []
for row in df['path'].values:
    img_path2 = img_path + row
    image = Image.open(img_path2)
    image = transforms.ToTensor()(image).unsqueeze(0)
    image = image[:,:,0:348,0:348]
    train_x.append(image)
    target = row.split('/')[2]
    train_y.append(target)

with open("train_x.txt", "wb") as fp:   #Pickling
    pickle.dump(train_x, fp)

with open("train_y.txt", "wb") as fp:   #Pickling
    pickle.dump(train_y, fp)


test_x = []
test_y = []
for row in df['path'].values:
    img_path2 = img_path + row
    image = Image.open(img_path2)
    image = transforms.ToTensor()(image).unsqueeze(0)
    image = image[:,:,0:348,0:348]
    test_x.append(image)
    target = row.split('/')[2]
    test_y.append(target)

with open("test_x.txt", "wb") as fp:   #Pickling
    pickle.dump(test_x, fp)

with open("test_y.txt", "wb") as fp:   #Pickling
    pickle.dump(test_y, fp)