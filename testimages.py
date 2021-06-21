import torch
from torchvision import transforms
import os
import pandas as pd
from PIL import Image
from imagerecognition import ModifiedAlexNet

cwd = os.getcwd()
img_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/')
#img_path2 = img_path + '/test/Fruit/Melon/Watermelon/Watermelon_044.jpg'
#img_path2 = img_path + '/test/Packages/Milk/Arla-Lactose-Medium-Fat-Milk/Arla-Lactose-Medium-Fat-Milk_001.jpg'
#img_path2 = img_path + 'test/Vegetables/Potato/Floury-Potato/Floury-Potato_016.jpg'
#img_path2 = img_path + 'test/Fruit/Avocado/Avocado_030.jpg'


image = Image.open(img_path2)
image = transforms.ToTensor()(image).unsqueeze(0)
image = image[:,:,0:348,0:348]

df = pd.read_csv(img_path + '/clean_classes.csv')


model_name = "seventh_model.pt"
model = torch.load(model_name, map_location=torch.device('cpu'))

print(image.size())

predictions = model(image)
#(1, 43)
print(predictions.shape)
#Gives you the class number
class_number = int(torch.argmax(predictions))
print(class_number)
#Gives you the class name


ClassRow = df.loc[df['Coarse Class ID (int)'] == class_number]
print(ClassRow)
ClassString = ClassRow['Coarse Class Name (str)']

print(ClassString)