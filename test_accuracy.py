import torch
from torchvision.transforms import functional as F
from PIL import Image
from tqdm import tqdm
import os

# Load YOLOv8 model
model_path = "home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTIO/yolov8/custom_dataset/yolov8m-seg-custom.pt"
model = torch.load(model_path, map_location=torch.device('cpu'))['model'].float()
model.eval()

# Function to perform object detection
def detect_objects(image):
    image = image.unsqueeze(0)  # Add batch dimension
    pred = model(image)[0]
    return pred

# Expected input size of the YOLOv8 model
input_size = (640, 640)  # Adjust according to the model's input size

# Path to test images folder
test_folder = "ome/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTIO/yolov8/custom_dataset/test"

# Calculate average confidence score
total_confidence = 0.0
total_predictions = 0

for image_file in tqdm(os.listdir(test_folder)):
    image_path = os.path.join(test_folder, image_file)
    image = Image.open(image_path)

    # Resize image if necessary
    if image.size != input_size:
        image = image.resize(input_size)

    image_tensor = F.to_tensor(image).float()  # Convert image to tensor
    with torch.no_grad():
        detections = detect_objects(image_tensor)

    for det in detections:
        # Extract confidence score from the detection results
        confidence_score = det[4].max().item()  # Confidence score is the maximum class probability
        total_confidence += confidence_score
        total_predictions += 1

average_confidence = total_confidence / total_predictions

print("Average confidence score:", average_confidence)
