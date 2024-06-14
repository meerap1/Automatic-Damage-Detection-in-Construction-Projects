import cv2
import os
import numpy as np

# Define directories
img_dir = '/home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTION/yolov8/custom_dataset/train5/images'
label_dir = '/home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTION/yolov8/custom_dataset/train5/labels'
augmented_image_dir = '/home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTION/yolov8/custom_dataset/train6/images'
augmented_label_dir = '/home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTION/yolov8/custom_dataset/train6/labels'

# Define augmentation parameters
rotation_angles = [0, 90, 180, 270]
flip_modes = [0, 1, -1]  # 0: flip vertically, 1: flip horizontally, -1: flip both vertically and horizontally

# Function to apply augmentation and save images and labels
def augment_and_save(image_path, label_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Load corresponding label
    label = np.loadtxt(label_path)
    
    # Apply augmentation
    for angle in rotation_angles:
        rotated_image = cv2.rotate(image, angle)
        
        for mode in flip_modes:
            flipped_image = cv2.flip(rotated_image, mode)
            
            # Save augmented image
            augmented_image_name = os.path.basename(image_path).split('.')[0] + f'_rot{angle}_flip{mode}.jpg'
            augmented_image_path = os.path.join(augmented_image_dir, augmented_image_name)
            cv2.imwrite(augmented_image_path, flipped_image)
            
            # Adjust label coordinates if necessary (e.g., for rotation)
            # Save augmented label
            augmented_label_name = os.path.basename(label_path).split('.')[0] + f'_rot{angle}_flip{mode}.txt'
            augmented_label_path = os.path.join(augmented_label_dir, augmented_label_name)
            np.savetxt(augmented_label_path, label)  # Save label as is (no transformation)

            print(f"Augmented image and label saved: {augmented_image_path}, {augmented_label_path}")

# Loop through each image in the image directory
for image_name in os.listdir(img_dir):
    # Check if corresponding label exists
    label_name = image_name.replace('.jpg', '.txt')
    label_path = os.path.join(label_dir, label_name)
    if os.path.exists(label_path):
        image_path = os.path.join(img_dir, image_name)
        augment_and_save(image_path, label_path)
    else:
        print(f"No label found for image: {image_name}")

