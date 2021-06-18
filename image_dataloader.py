import os
import torch
import numpy
import pandas as pd
import pytorch_lightning as pl

from pprint import pprint as pp
from PIL import Image
from torchvision import transforms

class GroceryStoreDataset(torch.utils.data.Dataset):
    def __init__(self, 
                 images_root_path: str, 
                 csv_path: str,
                 img_height: int,
                 img_width: int):
        super().__init__()

        self.images_list = []
        self.labels_list = []

        self.csv = pd.read_csv(csv_path, 
                                 delimiter = ',', 
                                 names=["path", "precision", "name"])

        for row, label in zip(self.csv['path'].values, self.csv['name'].values):

            image_path = os.path.join(images_root_path, row)

            self.images_list.append(image_path)
            self.labels_list.append(label)

        self.transforms = transforms.Compose([
                #transforms.RandomHorizontalFlip(),
                #transforms.ToPILImage(),
                transforms.Resize((img_height, img_width)),
                transforms.ToTensor()
            ])

    def __len__(self):
        return len(self.images_list)

    def __getitem__(self, idx: int):
        image = Image.open(self.images_list[idx])
        image = self.transforms(image)

        label = self.labels_list[idx]

        return image, label

class GroceryStoreDataloader(pl.LightningDataModule):
    def __init__(self,
                 images_root_path: str, 
                 train_csv_path: str,
                 val_csv_path: str,
                 test_csv_path:str,
                 img_height: int,
                 img_width: int,
                 batch_size: int,
                 num_workers):
        super().__init__()

        self.images_root_path = images_root_path
        self.train_csv_path = train_csv_path
        self.val_csv_path = val_csv_path
        self.test_csv_path = test_csv_path
        self.img_height = img_height
        self.img_width = img_width
        self.batch_size = batch_size
        self.num_workers = num_workers

    def prepare_data(self):
        pass

    def setup(self, stage='fit'):

        self.train_dataset = GroceryStoreDataset(self.images_root_path,
                                            self.train_csv_path,
                                            self.img_height,
                                            self.img_width)

        self.val_dataset = GroceryStoreDataset(self.images_root_path,
                                            self.val_csv_path,
                                            self.img_height,
                                            self.img_width)

        self.test_dataset = GroceryStoreDataset(self.images_root_path,
                                            self.test_csv_path,
                                            self.img_height,
                                            self.img_width)

    def train_dataloader(self):
        return torch.utils.data.DataLoader(
            self.train_dataset,
            batch_size=self.batch_size,
            drop_last=True,
            num_workers=self.num_workers)


    def val_dataloader(self):
        return torch.utils.data.DataLoader(
            self.val_dataset,
            batch_size=self.batch_size,
            drop_last=True,
            num_workers=self.num_workers)

    def test_dataloader(self):
        return torch.utils.data.DataLoader(
            self.test_dataset,
            batch_size=self.batch_size,
            drop_last=True,
            num_workers=self.num_workers)

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

    dataloader = GroceryStoreDataloader(images_root_path, 
                                        train_csv_path,
                                        val_csv_path,
                                        test_csv_path,
                                        img_height, 
                                        img_width, 
                                        batch_size, 
                                        num_workers)

    dataloader.setup()

    train_dataloader = dataloader.train_dataloader()

    images, labels = next(iter(train_dataloader))

    pp(images.shape)
    pp(labels.shape)
    