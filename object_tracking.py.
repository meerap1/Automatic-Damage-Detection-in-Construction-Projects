import os
import cv2

# Set the directory path where images are located
directory = r'F:\Projects\Project_videos\bridge_86_shimoga\extracted_frames\Pier-3_Line-18___QGC_30-12-2021_2_7_1_'

# Get all image filenames in the directory
image_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.jpg')]

print("Number of image files found:", len(image_files))  # Debug print

if not image_files:
    print("No image files found in the directory. Please verify the directory path and file extensions.")
    exit()

tracker = cv2.TrackerKCF_create()

# Read the first image
first_image_path = image_files[0]
frame = cv2.imread(first_image_path)
bbox = cv2.selectROI(frame)
ok = tracker.init(frame, bbox)

# Create a directory to save tracked images
output_directory = os.path.join(directory, 'tracked_images')
os.makedirs(output_directory, exist_ok=True)

# Iterate over each image starting from the second one
for image_path in image_files[1:]:
    frame = cv2.imread(image_path)
    
    # Update tracker with the new frame
    ok, bbox = tracker.update(frame)
    if ok:
        (x, y, w, h) = [int(v) for v in bbox]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2, 1)
        # Save the tracked image
        output_path = os.path.join(output_directory, os.path.basename(image_path))
        cv2.imwrite(output_path, frame)
    else:
        cv2.putText(frame, 'Error', (100, 0), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    cv2.imshow('Tracking', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Close all OpenCV windows
cv2.destroyAllWindows()
