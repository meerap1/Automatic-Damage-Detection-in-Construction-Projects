import os
import random
import shutil

# Define paths to source folders
images_folder = "F:/Projects/Data for damage detection in concrete structures-20240208T060819Z-001/Processed data/img"
labels_folder = "F:/Projects/Data for damage detection in concrete structures-20240208T060819Z-001/Processed data/lab"

# Define paths to destination folders
train_folder = "F:/Projects/train"
test_folder = "F:/Projects/test"
validate_folder = "F:/Projects/validate"

# Create destination folders if they don't exist
for folder in [train_folder, test_folder, validate_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# Get list of files in source folders
image_files = [f for f in os.listdir(images_folder) if os.path.isfile(os.path.join(images_folder, f))]
label_files = [f for f in os.listdir(labels_folder) if os.path.isfile(os.path.join(labels_folder, f))]

# Shuffle the files
random.shuffle(image_files)
random.shuffle(label_files)

# Define split sizes
train_split = int(0.7 * len(image_files))
test_split = int(0.2 * len(image_files))
validate_split = len(image_files) - train_split - test_split

# Split files into train, test, and validate sets
train_images = image_files[:train_split]
test_images = image_files[train_split:train_split + test_split]
validate_images = image_files[train_split + test_split:]

train_labels = [f.replace('.png', '.txt').replace('.jpeg', '.txt').replace('.jpg', '.txt') for f in train_images]
test_labels = [f.replace('.png', '.txt').replace('.jpeg', '.txt').replace('.jpg', '.txt') for f in test_images]
validate_labels = [f.replace('.png', '.txt').replace('.jpeg', '.txt').replace('.jpg', '.txt') for f in validate_images]

# Move files to destination folders
for src, dest in zip(train_images, train_labels):
    shutil.copy(os.path.join(images_folder, src), os.path.join(train_folder, src))
    shutil.copy(os.path.join(labels_folder, dest), os.path.join(train_folder, dest))

for src, dest in zip(test_images, test_labels):
    shutil.copy(os.path.join(images_folder, src), os.path.join(test_folder, src))
    shutil.copy(os.path.join(labels_folder, dest), os.path.join(test_folder, dest))

for src, dest in zip(validate_images, validate_labels):
    shutil.copy(os.path.join(images_folder, src), os.path.join(validate_folder, src))
    shutil.copy(os.path.join(labels_folder, dest), os.path.join(validate_folder, dest))

print("Data splitting completed successfully.")

