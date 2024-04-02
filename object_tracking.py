import os
import cv2
import numpy as np

# Set the directory path where images are located
directory = r'F:\Projects\Project_videos\bridge_86_shimoga\extracted_frames\Pier-3_Line-18___QGC_30-12-2021_2_7_1_'

# Get all image filenames in the directory
image_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.jpg')]

tracker = cv2.TrackerKCF_create()

# Iterate over each image
for image_path in image_files:
    frame = cv2.imread(image_path)
    bbox = cv2.selectROI(frame)
    ok = tracker.init(frame, bbox)
    
    while True:
        ok, frame = True, cv2.imread(image_path)  # For images, 'ok' is always True, and we read the image again
        if not ok:
            break
        
        ok, bbox = tracker.update(frame)
        if ok:
            (x, y, w, h) = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
        else:
            cv2.putText(frame, 'Error', (100, 0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        cv2.imshow('Tracking', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

# Close all OpenCV windows
cv2.destroyAllWindows()
