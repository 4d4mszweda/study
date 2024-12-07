import os
import shutil
from sklearn.model_selection import train_test_split

def create_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def split_data(source_folder, train_folder, validation_folder, test_size=0.2):
    categories = ['cats', 'dogs']
    
    for category in categories:
        category_path = os.path.join(source_folder, category)
        images = [os.path.join(category_path, img) for img in os.listdir(category_path) if os.path.isfile(os.path.join(category_path, img))]
        
        train_images, val_images = train_test_split(images, test_size=test_size, random_state=42)
        
        train_category_path = os.path.join(train_folder, category)
        val_category_path = os.path.join(validation_folder, category)
        
        create_dir(train_category_path)
        create_dir(val_category_path)
        
        for img in train_images:
            shutil.copy(img, train_category_path)
        
        for img in val_images:
            shutil.copy(img, val_category_path)

if __name__ == "__main__":
    source_folder = './dogs-cats-mini'
    train_folder = './dataset/train'
    validation_folder = './dataset/validation'
    
    split_data(source_folder, train_folder, validation_folder, test_size=0.2)