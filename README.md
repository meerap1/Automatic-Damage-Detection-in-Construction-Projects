# Automatic-Damage-Detection-in-Construction-Projects
## Table of Content
1. Introduction
2. Data Collection
3. Annotation using Yolo annotation tool
4. Conversion of JSON to yolo label format
## Introduction
Automatic Damage Detection in Underwater Construction is a critical endeavor aimed at leveraging machine learning and computer vision technologies to detect and classify various forms of damage in submerged structures. By harnessing advanced algorithms and image processing techniques, this project seeks to enhance inspection and maintenance processes, ensuring the structural integrity and safety of underwater constructions. Through automated detection, the project aims to mitigate risks, reduce inspection times, and enable timely interventions, thereby contributing to the sustainability and resilience of underwater infrastructure.
## Data Collection
Data has been meticulously collected from various underwater structures including the Shimoga bridge, KR Nagar bridge, KRS Dam, Shirawata Dam, Sholayar Dam, and Vani Vilasa Sagar Dam, employing Remotely Operated Vehicles (ROVs) for precise and comprehensive inspections. These ROVs have facilitated the acquisition of high-resolution imagery and video footage, capturing detailed information about the structural conditions of the submerged infrastructure. Leveraging this extensive dataset, the project aims to develop a robust machine learning model for automatic damage detection. By analyzing the collected data, the model seeks to identify and classify different types of damages such as cracks, displacement, and material degradation. This initiative holds the potential to revolutionize underwater construction inspection practices, enabling early detection of structural issues and proactive maintenance measures to ensure the longevity and safety of these vital infrastructural assets.
## Annotation using Yolo annotation tool
The YOLO annotation tool facilitates the annotation process by assigning numerical labels to different classes of features within images. Each class is assigned a unique numerical label based on its position in the list, starting from 0. For instance, "Unintended Eccentricities" is designated as class label 0, while "Reinforcement Spotted" is assigned class label 30. This mapping of classes to labels allows the model to accurately identify and classify various features within the images. By associating specific numerical labels with each class, the YOLO annotation tool streamlines the annotation process, ensuring that the model can effectively detect and classify different types of damage in underwater construction projects.

##### Unintended Eccentricities - Class label: 0
##### Loss of Material - Class label: 1
##### Displacement of stones - Class label: 2
##### Reinforcement Exposed - Class label: 3
##### Cracks - Class label: 4
##### Sourcing and Deteriorated Stones - Class label: 5
##### Loss of Material with reinforcement exposed - Class label: 6
##### Cavities - Class label: 7
##### Concrete degradation and exposed reinforcement - Class label: 8
##### Mild cavities - Class label: 9
##### Concrete degradation - Class label: 10
##### Honey Combing - Class label: 11
##### Deteriorated Stones/bricks - Class label: 12
##### Deteriorated joint - Class label: 13
##### Loss of pointing Mortar - Class label: 14
##### Presence of debris/Rocks/Tree-Trunks - Class label: 15
##### Minor cavity - Class label: 16
##### Loss of pointing mortar and deposits of debris - Class label: 17
##### Distressed Joints - Class label: 18
##### Unintended Eccentricities P1 Highlight - Class label: 19
##### Material Deterioration/ Delamination - Class label: 20
##### Material disintegration - Class label: 21
##### Spalling of gunniting - Class label: 23
##### Deposits of debris/Rocks/Tree-Trunks - Class label: 24
##### Abrasion - Class label: 25
##### Pipe/debris noted - Class label: 28
##### Material Loss/Disintegration - Class label: 29
##### Reinforcement Spotted - Class label: 30.
## Conversion of JSON to yolo label format
JSON data contains coordinates of detected damages in images, crucial for bounding these damages. These coordinates are converted into YOLO labels, which are bounding boxes representing the damages. YOLO, a fast and accurate object detection system, is trained using these labels to recognize and locate damages effectively. Each damage type in JSON is matched with a YOLO label for training. This process ensures YOLO can identify and classify damages accurately. Once mapped, the JSON data aids in training the YOLO model for efficient damage detection. If the JSON data indicates "Loss of Material" damage, it will be assigned class label 1 in YOLO. Similarly, each unique damage type in the JSON data is mapped to its corresponding YOLO class label. Once the JSON data is mapped to YOLO labels, it can be used in training the YOLO model.

