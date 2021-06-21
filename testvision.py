import torch
from torchvision import transforms
import os
import pandas as pd
from PIL import Image

def food_vision(test_img_path):
    #to open the image from the given path
    cwd = os.getcwd()
    img_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/')
    test_img_path = img_path + test_img_path
    image = Image.open(test_img_path)
    #Transforming the image to Tensor
    image = transforms.ToTensor()(image).unsqueeze(0)
    image = image[:,:,0:348,0:348]

    #to search for image class
    df = pd.read_csv(img_path + '/clean_classes.csv')

    #CNN model
    model_name = "fifth_model.pt"
    model = torch.load(model_name)

    #to ge the image size
    #print(image.size())

    #to predict the image class
    predictions = model(image)
    #(1, 43)

    #getting the prediction
    #print(predictions.shape)

    #Gives you the class number
    class_number = int(torch.argmax(predictions))
    #print(class_number)

    #Gives you the class name
    ClassRow = df.loc[df['Coarse Class ID (int)'] == class_number]
    #print(ClassRow)
    ClassString = ClassRow['Coarse Class Name (str)']

    return ClassString.to_string(index=False)