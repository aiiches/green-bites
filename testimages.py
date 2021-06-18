import torch
from torchvision import transforms
import os
import pandas as pd
from PIL import Image

cwd = os.getcwd()
img_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/')
img_path2 = img_path + '/test/Fruit/Melon/Watermelon/Watermelon_044.jpg'
image = Image.open(img_path2)
image = transforms.ToTensor()(image).unsqueeze(0)
image = image[:,:,0:348,0:348]

df = pd.read_csv(img_path + '/clean_classes.csv')

print(df)

'''
model_name = "first_model.pt"
model = torch.load(model_name)

print(image.size())

predictions = model (image)
#(1, 43)
print(predictions.shape)
#Gives you the class number
class_number = torch.argmax(predictions)
#Gives you the class name

Class_name = list_of_class_names[class_number]
'''