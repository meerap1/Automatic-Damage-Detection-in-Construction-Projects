import os

# Directory containing the label files
label_dir = '/home/eyerov/Documents/DAMAGE-DETECTION-IN-CONSTRUCTION/yolov8/custom_dataset/train5/labels'

# Initialize counts for digits 0, 1, and 2
counts = {'0': 0, '1': 0, '2': 0}

# Iterate over each label file
for filename in os.listdir(label_dir):
    label_path = os.path.join(label_dir, filename)
    with open(label_path, 'r') as file:
        # Read the first line
        first_line = file.readline().strip()
        # Check if the line is not empty and contains at least one character
        if first_line and first_line[0].isdigit():
            # Extract the first digit
            first_digit = first_line.split()[0]
            # Update the count based on the first digit
            if first_digit in counts:
                counts[first_digit] += 1

# Print the counts
print("Count of 0s:", counts['0'])
print("Count of 1s:", counts['1'])
print("Count of 2s:", counts['2'])

