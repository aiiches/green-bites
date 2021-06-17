# -*- coding: utf-8 -*-
"""ImageRecognition.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dP2MaSyoYMCeKhvNfEk8_RTPTEl4xHVQ
"""


import torch.nn as nn
import torch.optim as optim
from torchvision import transforms, models
import image_dataloader
import os

def train(epoch):
    model.train()
    tr_loss = 0
    # getting the training set
    for batch in train_dataloader:
        images, labels = batch
        # clearing the Gradients of the model parameters
        optimizer.zero_grad()
        # prediction for training set
        output_train = model(images)
        # computing the training loss
        loss_train = lossfun(output_train, labels)
        train_losses.append(loss_train)
        # computing the updated weights of all the model parameters
        loss_train.backward()
        optimizer.step()
        tr_loss = loss_train.item()


def validation(epoch):
    total_loss = 0
    for batch in val_dataloader:
        images, labels = batch
        output_val = model(images)
        loss_train = lossfun(output_val, labels)
        total_loss += loss_train
    return(total_loss)
    
model = models.alexnet(pretrained = True)

# Let's define an optimizer

optimizer = optim.Adam(model.parameters(), lr=0.001)

# Let's define a Loss function

lossfun = nn.NLLLoss()  # Use nn.CrossEntropyLoss with softmax

if __name__ == '__main__':
    cwd = os.getcwd()

    images_root_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/')
    train_csv_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/train.txt')
    val_csv_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/val.txt')
    test_csv_path = os.path.join(cwd, 'data/GroceryStoreDataset-master/dataset/test.txt')
    img_height = 348
    img_width = 348
    batch_size = 32
    num_workers = 4

    dataloader = image_dataloader.GroceryStoreDataloader(images_root_path,
                                        train_csv_path,
                                        val_csv_path,
                                        test_csv_path,
                                        img_height,
                                        img_width,
                                        batch_size,
                                        num_workers)

    dataloader.setup()

    train_dataloader = dataloader.train_dataloader()
    val_dataloader = dataloader.val_dataloader()



# defining the number of epochs
n_epochs = 25
# empty list to store training losses
train_losses = []
# empty list to store validation losses
test_losses = []
# training the model
for epoch in range(n_epochs):
    train(epoch)
    print(validation(epoch))


