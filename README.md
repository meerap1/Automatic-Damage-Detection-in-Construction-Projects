# Automatic-Damage-Detection-in-Construction-Projects
![Untitled design](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/31afbcbd-8c92-469a-b32c-9fafd0bf535f)

## Table of Content
1. Introduction
2. Data Collection
3. Annotation using Yolo annotation tool
4. Conversion of JSON to yolo label format
5. Frames Extraction
6. Object Tracking
7. Data Augmentation
8. Model Building (Yolov7 Object Detection)
9. Model Building (Yolov8 Instance Segmentation)

## Introduction
Automatic Damage Detection in Underwater Construction is a critical endeavor aimed at leveraging machine learning and computer vision technologies to detect and classify various forms of damage in submerged structures. By harnessing advanced algorithms and image processing techniques, this project seeks to enhance inspection and maintenance processes, ensuring the structural integrity and safety of underwater constructions. Through automated detection, the project aims to mitigate risks, reduce inspection times, and enable timely interventions, thereby contributing to the sustainability and resilience of underwater infrastructure.
## Data Collection
Data has been meticulously collected from various underwater structures including the **Shimoga bridge, KR Nagar bridge, KRS Dam, Shirawata Dam, Sholayar Dam, and Vani Vilasa Sagar Dam**, employing Remotely Operated Vehicles (ROVs) for precise and comprehensive inspections. These ROVs have facilitated the acquisition of high-resolution imagery and video footage, capturing detailed information about the structural conditions of the submerged infrastructure. Leveraging this extensive dataset, the project aims to develop a robust machine learning model for automatic damage detection. By analyzing the collected data, the model seeks to identify and classify different types of damages such as cracks, displacement, and material degradation. This initiative holds the potential to revolutionize underwater construction inspection practices, enabling early detection of structural issues and proactive maintenance measures to ensure the longevity and safety of these vital infrastructural assets.

## Annotation using Yolo annotation tool
The YOLO annotation tool facilitates the annotation process by assigning numerical labels to different classes of features within images. Each class is assigned a unique numerical label based on its position in the list, starting from 0. For instance, "Unintended Eccentricities" is designated as class label 0, while "Reinforcement Spotted" is assigned class label 30. This mapping of classes to labels allows the model to accurately identify and classify various features within the images. By associating specific numerical labels with each class, the YOLO annotation tool streamlines the annotation process, ensuring that the model can effectively detect and classify different types of damage in underwater construction projects.
   
## Conversion of JSON to yolo label format
JSON data contains coordinates of detected damages in images, crucial for bounding these damages. These coordinates are converted into YOLO labels, which are bounding boxes representing the damages. YOLO, a fast and accurate object detection system, is trained using these labels to recognize and locate damages effectively. Each damage type in JSON is matched with a YOLO label for training. This process ensures YOLO can identify and classify damages accurately. Once mapped, the JSON data aids in training the YOLO model for efficient damage detection. If the JSON data indicates "Loss of Material" damage, it will be assigned class label 1 in YOLO. Similarly, each unique damage type in the JSON data is mapped to its corresponding YOLO class label. Once the JSON data is mapped to YOLO labels, it can be used in training the YOLO model.

## Frames Extraction
To increase the size and diversity of the training dataset for YOLO models, we extracted additional frames from underwater videos. We selected frames within a window from two seconds before to two seconds after keyframes. This approach captures the progression and context of key events, providing a comprehensive set of data points. The extracted frames help improve the dataset's quality and diversity, which is essential for effective model training.

## Object Tracking
To ensure consistent annotations across the extracted frames, we used object tracking. By applying advanced tracking algorithms, we followed objects through the frames from two seconds before to two seconds after keyframes. This method maintains accurate bounding boxes as objects move, ensuring the annotations are consistent. Consistent annotations are crucial for training robust YOLO models, as they help the model learn to detect objects more reliably.

## Data Augmentation
Data augmentation involves artificially expanding the size and diversity of a dataset by applying various transformations to existing data samples. This process enhances model generalization and performance by exposing it to a wider range of variations and scenarios. For our dataset, we applied transformations such as rotating images by various degrees and flipping them. These augmentations increased the dataset's variability, making it more robust and well-prepared for training the YOLO model.

## Model Building (Yolov7 Object Detection)
To create a model which detect one damage "**Loss of Pointing Mortar**" using anaconda prompt, we need to
### Creating Virtual Environement:
To create a virtual environment, open Anaconda Prompt and use the following code: <br/>
<br/>
`conda create -n yolov7_custom python=3.9` <br/>
<br/>
After hitting enter, type 'Y' and hit enter again. Once the environment is created, activate it with the command: <br/>
<br/>
`conda activate yolov7_custom` <br/>
<br/>
###  Setup Yolov7 Repository
Download the official YOLOv7 repository from the [link](https://github.com/WongKinYiu/yolov7) <br/>
<br/>
Download the zip file into your **yolov7_custom** folder. Once downloaded, unzip it and rename the folder to **yolov7_custom**. Then, move the folder to the main directory **yolov7_custom**and delete the empty directory. <br/>
<br/>
Inside the extracted repository, open the **requirements.txt** file. Check the Torch version; it should be greater than or equal to 1.7 but not 1.12. Similarly, the TorchVision version should be greater than or equal to 0.8.1 but not 0.13. Make note of these versions and visit the PyTorch website to install PyTorch with CUDA support, meeting the requirements listed in the txt files. <br/>
<br/>
![Screenshot 2024-04-16 115159](https://github.com/meerap1/FISH-DETECTION/assets/156745402/b0e2bf66-3340-48e4-bc3a-0f1cf753b797) <br/>
<br/>
Remove the lines referencing Torch and TorchVision from the 'requirements.txt' file, then save the file. Additionally, create a new text file and paste the pip install command used to install PyTorch with CUDA support. Ensure the command is correctly formatted, like so: <br/>
![Screenshot 2024-04-16 120410](https://github.com/meerap1/FISH-DETECTION/assets/156745402/d0187060-3507-4bc9-a362-e672b4788189)  <br/>
 <br/>
Save the file as **requirements_gpu.txt** <br/>
<br/>
Now, in Anaconda Prompt, navigate to the **yolov7_custom** directory and execute the command: <br/>
<br/>
`pip install -r requirements.txt` <br/>
<br/>
this will install all the libraries that are part of the requirements.txt once it is done execute another command <br/>
<br/>
`pip install -r requirements_gpu.txt` <br/>
<br/>
This will install PyTorch with CUDA support. <br/>
<br/>
### Modify Yolov7 Files
Now, the **train** and **validation** folders should be moved into the **data** folder inside the **yolov7_custom** directory. <br/>
<br/>
Now make a copy of coco.yaml file in the data folder and rename it to **custom_data.yaml** . open it and modify like below <br/>
<br/>
In the text file, we will modify the **train** and **val** paths. Also, **nc** represents the number of classes. In this case, we have only one class, which is **Loss of Pointing Mortar**, and it is mentioned in the **names**. <br/>
<br/>
![image](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/44b80d23-a97f-45a9-ad9f-66bc20da0471) <br/>
<br/>
Now, open the **training** folder in the **cfg** folder. Inside, you'll find 7 configuration files. You can choose any of them to train the Loss of Pointing Mortar dataset. In this case, we are selecting **yolov7.yaml**. Make a copy of this file. In the copied file, change only **nc** to 1 as we are having only one class, and then save it. <br/>
<br/>
![Screenshot 2024-04-16 130749](https://github.com/meerap1/FISH-DETECTION/assets/156745402/53cfd46b-5c8b-40e5-ba79-932575a57e0a) <br/>
<br/>
Now, we need to download the weights for the YOLOv7 base model from the official YOLOv7 repository. It is hidden in the [releases](https://github.com/WongKinYiu/yolov7/releases). Here, I downloaded **yolov7.pt** and copied it to the yolov7_custom directory. <br/>
<br/>
### Train Yolov7 Model
Open Anaconda Prompt, ensure you're in the **yolov7_custom** directory, and run the following command: <br/>
<br/>
`python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7_custom.yaml --name yolov7_custom --weights yolov7.pt` <br/>
<br/>
When the training is finished, you can find the training files in the yolov7_custom folder from runsin the main yolov7_custom directory. Additionally, within that directory, you'll find the 'weights' folder. Inside the 'weights' folder, locate the **best.pt** file, which represents the best weights based on the validation loss. Copy and paste this file to the main directory of 'yolov7_custom' and rename it to '**yolov7_custom.pt**'.

### Testing on Images and Videos
Copy a test image and video and move them to the main directory 'yolov7_custom'. Rename the image to **1.jpg** and the video to **1.mp4**. Then, run the following command: <br/>
<br/>
`python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source 1.jpg --view-img --no-trace` <br/>
<br/>
`python detect.py --weights yolov7_custom.pt --conf 0.5 --img-size 640 --source 1.mp4 --view-img --no-trace` <br/>
<br/>
The output will be saved in the 'exp' folder within the 'detect' directory under 'runs'.
### Results
Utilized evaluation metrics such as Confusion Matrix and F1 Curve. The model successfully detected 'Loss of Pointing Mortar' in 69% of cases where it was present and correctly identified its absence in all cases, but it showed a 31% false alarm rate. Improvement is needed to reduce false alarms and enhance overall accuracy.
![confusion_matrix](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/f703f42a-07b3-4a7e-bf1d-0b37dc59a1e6)
![BoxF1_curve (2)](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/05e9b5c5-4dd2-461a-b376-eb577c7b0318)
## Model Building (Yolov8 Instance Segmentation)
To create a model which detect damages "**Loss of Pointing Mortar**", "**Cavities**" and "**Reinforcement Exposed**" using google colab, we need to
## Data Segmentation:
Data segmentation is performed using Roboflow. The dataset includes 3 classes: "**Loss of Pointing Mortar**", "**Cavities**" and "**Reinforcement Exposed**". The data is divided into training and validation sets in a 80:20 ratio.
### Creating Virtual Environement:
First, change the runtime to **T4 GPU** and connect it. Then, check  to ensure that the GPU is properly configured and available for use. <br/>
<br/>
**`!nvidia-smi`** <br/>
<br/>
The following code is used to mount Google Drive in a Google Colab environment: <br/>
<br/>
**`from google.colab import drive`**<br/>
<br/>
**`drive.mount('/content/gdrive')`** <br/>
<br/>
The following commands are used to navigate directories in Google Colab environment:<br/>
<br/>
**`%cd yolov8`**<br/>
<br/>
**`%cd custom_dataset`** <br/>
<br/>
In the custom_dataset folder, we have training and validation datasets along with a data.yaml file. The data.yaml file typically contains information about the dataset, such as the number of classes, class names, and paths to the training and validation data. <br/>
<br/>
![image](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/dbf5264e-0878-4b42-9fee-29686aadfd54)


By navigating to this directory, we are setting up the environment to access and use these files for training the YOLOv8 model.
## Setup Yolov8 Repository
The following command installs the ultralytics package:<br/>
<br/>
**`!pip install ultralytics`** <br/>
## Train Yolov8 Model
The following command is used to train a YOLOv8 segmentation model:<br/>
<br/>
**`!yolo task=segment mode=train epochs=100 data=data.yaml model=yolov8m-seg.pt imgsz=640 batch=16`** <br/>
<br/>
This command initiates the training of a YOLOv8 segmentation model using the specified pre-trained model (yolov8m-seg.pt) on THE custom dataset defined in data.yaml, with the images resized to 640x640 pixels, and a batch size of 16 for 100 epochs. <br/>
<br/>
After the training process, the best-performing model weights are saved as best.pt in the directory runs/segment/train/weights/. This best.pt file represents the model with the highest validation performance during training. To utilize this trained model for future inference or further training, it is common practice to copy best.pt and paste it into the custom_data folder, renaming it to yolov8m-seg-custom.pt. This ensures that the most optimized version of the model is readily accessible and identified within the custom dataset directory.

## Testing on Images and Videos
To prepare for making predictions using a trained YOLOv8 segmentation model, create this py file in custom_dataset and name it predict.py.:<br/>
<br/>
![Screenshot 2024-05-24 015023](https://github.com/meerap1/Image-Segmentation-on-Custom-dataset/assets/156745402/da12e682-d816-4f9c-bd15-93f053285cc0) <br/>
<br/>
The output will be saved in the 'exp' folder within the 'detect' directory under 'runs'.

### Results
Utilized evaluation metrics such as Confusion Matrix and F1 Curve.Achieved high accuracy in detecting damages like Loss of Pointing Mortar (93%), Cavities (95%), and Reinforcement Exposed (82%) for damage detection using Instance Segmentation. 
![confusion_matrix_normalized (1)](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/ebeaa229-a733-42a6-9394-7d7690fbeab3)
![BoxF1_curve (1)](https://github.com/meerap1/Automatic-Damage-Detection-in-Construction-Projects/assets/156745402/d91d0b26-24ff-487d-b0c3-5ac31721cb0f)

### Inference
Background detection indicates areas for enhancement.
