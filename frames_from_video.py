import cv2
import json
import os

def extract_frames(video_path, output_folder, position_seconds):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Load positions from JSON
    with open(position_seconds, 'r') as json_file:
        positions = json.load(json_file)

    # Extract frames
    cap = cv2.VideoCapture(video_path)
    for entry in positions:
        timestamp_str = entry.get('damage_ref', {}).get('damage_time_ms_ref', '')  # Get timestamp as string, or empty string if not found
        if timestamp_str:  # Check if the value is not empty
            try:
                timestamp = int(timestamp_str) / 1000  # Convert to integer before division
                cap.set(cv2.CAP_PROP_POS_MSEC, (timestamp - 5) * 1000)  # Move 5 seconds back
                success, image = cap.read()
                if success:
                    frame_name = f"frame_{entry['_id']}.jpg"
                    cv2.imwrite(os.path.join(output_folder, frame_name), image)
                    print(f"Frame extracted for entry {entry['_id']}")
                else:
                    print(f"Error extracting frame for entry {entry['_id']}")

                cap.set(cv2.CAP_PROP_POS_MSEC, (timestamp + 5) * 1000)  # Move 5 seconds forward
                success, image = cap.read()
                if success:
                    frame_name = f"frame_{entry['_id']}_after.jpg"
                    cv2.imwrite(os.path.join(output_folder, frame_name), image)
                    print(f"Frame extracted after for entry {entry['_id']}")
                else:
                    print(f"Error extracting frame after for entry {entry['_id']}")
            except ValueError:
                print(f"Error converting timestamp to integer for entry {entry['_id']}")
        else:
            print(f"Skipping entry {entry['_id']} due to empty timestamp")

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    video_path = r'F:\Projects\Damage or Not\Raw files\vani_vilasa_sagar_dam_er38-ka-dm-5-ubp-2022-23-1\projectFiles\videos\Line-31____QGC_31-12-2022_7_5_5_.mp4'
    output_folder = r'F:\Projects\Damage or Not\ExtractedFrames'
    position_seconds = r'F:\Projects\Damage or Not\Raw files\vani_vilasa_sagar_dam_er38-ka-dm-5-ubp-2022-23-1\projectFiles\damageList.json'

    extract_frames(video_path, output_folder, position_seconds)
