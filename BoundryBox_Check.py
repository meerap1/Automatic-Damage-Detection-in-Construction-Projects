import os
import cv2

# Function to read annotations from YOLO format txt files
def read_annotations(annotation_file, image_width, image_height):
    with open(annotation_file, 'r') as file:
        lines = file.readlines()
        annotations = []
        for line in lines:
            class_label, x_center, y_center, width, height, *_ = map(float, line.strip().split())
            # Convert normalized coordinates to pixel coordinates
            x1 = int((x_center * image_width) - (width * image_width / 2))
            y1 = int((y_center * image_height) - (height * image_height / 2))
            x2 = int((x_center * image_width) + (width * image_width / 2))
            y2 = int((y_center * image_height) + (height * image_height / 2))
            annotations.append([x1, y1, x2, y2])
    return annotations

# Function to mark annotations on the image
def mark_annotations(image_path, annotations):
    image = cv2.imread(image_path)
    for annotation in annotations:
        x1, y1, x2, y2 = annotation
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Light green color
    return image

# Paths to image and annotation folders
image_folder = r'F:\Projects\Data for damage detection in concrete structures-20240208T060819Z-001\Raw data - Copy\vani_vilasa_sagar_dam_er38-ka-dm-5-ubp-2022-23-1\Damage Images\img'
annotation_folder = r'F:\Projects\Data for damage detection in concrete structures-20240208T060819Z-001\Raw data - Copy\vani_vilasa_sagar_dam_er38-ka-dm-5-ubp-2022-23-1\Damage Images\lab'
output_folder = r'F:\Projects\Data for damage detection in concrete structures-20240208T060819Z-001\Raw data - Copy\vani_vilasa_sagar_dam_er38-ka-dm-5-ubp-2022-23-1\Damage Images\highlights'

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Process each image and its corresponding annotation
for image_file in os.listdir(image_folder):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        image_path = os.path.join(image_folder, image_file)
        annotation_file = os.path.join(annotation_folder, os.path.splitext(image_file)[0] + '.txt')

        if os.path.exists(annotation_file):
            # Read image dimensions
            image = cv2.imread(image_path)
            image_height, image_width, _ = image.shape

            # Read annotations
            annotations = read_annotations(annotation_file, image_width, image_height)
            annotated_image = mark_annotations(image_path, annotations)

            # Save the annotated image
            output_path = os.path.join(output_folder, image_file)
            cv2.imwrite(output_path, annotated_image)

            print(f"Annotated image saved: {output_path}")

print("All images processed and annotated.")
