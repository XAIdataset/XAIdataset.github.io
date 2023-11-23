import os
import json
import numpy as np
from PIL import Image
import pandas as pd
from torch.utils.data import Dataset
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split

class MultiFolderDataset(Dataset):
    def __init__(self, folder_paths, attention_path, transform=None):
        self.folder_paths = folder_paths
        self.attention_paths = attention_path
        self.transform = transform
        self.image_names, self.image_paths = self._get_image_paths()
        self.attention_df = self._get_attention_df()
    
    def _get_image_paths(self):
        names = []
        paths = []
        for folder_path in self.folder_paths:
            for filename in os.listdir(folder_path):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    names.append(filename)
                    paths.append(os.path.join(folder_path, filename))
        return names, paths
    
    def _get_attention_df(self):
        dataframes = []
        for filename in os.listdir(self.attention_paths):
            if filename.endswith('.csv'):
                filepath = os.path.join(self.attention_paths, filename)
                df = pd.read_csv(filepath)
                dataframes.append(df)
        combined_df = pd.concat(dataframes, ignore_index=True)
        return combined_df
    
    def _get_attention_for_image(self, image_name):
        unit_df = self.attention_df[self.attention_df["img_idx"] == image_name]
        if unit_df.empty:
            attention = np.zeros((224, 224))
        else:            
            attention_string = unit_df.attention.values[0]
            attention = np.array(json.loads(attention_string))
        return attention

    def __len__(self):
        return len(self.image_paths)
    
    def __getitem__(self, index):
        image_name = self.image_names[index]
        image_path = self.image_paths[index]
        image = Image.open(image_path)
        attention = self._get_attention_for_image(image_name)
        
        if self.transform:
            image = self.transform(image)
        
        # Extract the label from the folder path
        for i, folder_path in enumerate(self.folder_paths):
            if image_path.startswith(folder_path):
                label = i
                break
        
        return image, attention, label

def loading(dataset, class_list):
    print("Loading data...")
    root_dir = './Benchmarks/' + dataset + '/'
    folder_paths = [root_dir + 'image/' + item for item in class_list.split(',')]
    attention_path = root_dir + "attention_label"
    
    # Define your image transformations
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Lambda(lambda x: x[:3, :, :]),  # Keep only the first three channels
    ])
    
    dataset = MultiFolderDataset(folder_paths, attention_path, transform=transform)
    
    # Compute the sizes of each split
    train_ratio = 0.6  # 60% for training
    val_ratio = 0.2   # 20% for validation, and the rest for test

    train_size = int(train_ratio * len(dataset))
    val_size = int(val_ratio * len(dataset))
    test_size = len(dataset) - train_size - val_size
    
    print("Splitting dataset...")
    train_dataset, val_dataset, test_dataset = random_split(dataset, [train_size, val_size, test_size])

    # Create dataloaders for each split
    print("Creating dataloaders...")
    train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    val_dataloader = DataLoader(val_dataset, batch_size=32, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=True)
    
    print("Data loading complete.")
    return train_dataloader, val_dataloader, test_dataloader

