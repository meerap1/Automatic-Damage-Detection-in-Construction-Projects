import os
import json

def convert_to_yolo(json_file, output_folder):
    with open(json_file, 'r') as f:
        data = json.load(f)

    for entry in data:
        damage_ref = entry.get('damage_ref', {})
        damage_area_canvas = damage_ref.get('damage_area_canvas')

        if damage_area_canvas is not None:
            image_file_name = damage_area_canvas.get('image_file_name', '')
            image_file_name_without_canvas = image_file_name.replace('_canvas.jpg', '')

            labels_file_path = os.path.join(output_folder, image_file_name_without_canvas + '.txt')
            with open(labels_file_path, 'w') as labels_file:
                rects_config = damage_area_canvas.get('rects_config', [])

                for rect in rects_config:
                    x_min = rect.get('x', 0)
                    y_min = rect.get('y', 0)
                    width = rect.get('width', 0)
                    height = rect.get('height', 0)

                    # Calculate x_center, y_center, width_normalized, height_normalized
                    x_center = (x_min + width / 2) / damage_area_canvas.get('canvas_width', 1)
                    y_center = (y_min + height / 2) / damage_area_canvas.get('canvas_height', 1)
                    width_normalized = width / damage_area_canvas.get('canvas_width', 1)
                    height_normalized = height / damage_area_canvas.get('canvas_height', 1)

                    # Write YOLO label in the specified format
                    labels_file.write(f"0 {x_center} {y_center} {width_normalized} {height_normalized}\n")

# Example usage
json_file = 'damageList.json'
output_folder = 'labels'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

convert_to_yolo(json_file, output_folder)
