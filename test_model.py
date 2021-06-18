import torch
import os
import pandas as pd



import image_dataloader
"""
PATH = "model.pt"
model = torch.load(PATH)
model.eval()
"""

"""
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
    num_classes = 43

    print("Initializing dataloader")
    dataloader = image_dataloader.GroceryStoreDataloader(images_root_path,
                                        train_csv_path,
                                        val_csv_path,
                                        test_csv_path,
                                        img_height,
                                        img_width,
                                        batch_size,
                                        num_workers)

    dataloader.setup()

    test_dataloader = dataloader.test_dataloader()


"""
