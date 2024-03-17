import json
import os
import subprocess

def extract_frames(video_path, output_folder, start_time, end_time):
    # Use ffmpeg to extract frames
    subprocess.call([
    'ffmpeg',
    '-i', video_path,
    '-ss', str(start_time),
    '-to', str(end_time),
    '-vsync', '0',     # Disable frame dropping
    os.path.join(output_folder, 'frame_%04d.png')
])

def main():
    json_file_path = r'F:\Projects\Project_videos\bridge_86_shimoga\damageList.json'
    video_folder = r'F:\Projects\Project_videos\bridge_86_shimoga\videos\damage videos'
    output_base_folder = r'F:\Projects\Project_videos\bridge_86_shimoga\extracted_frames'

    # Load JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    # Process each entry
    for entry in data:
        video_name = entry['damage_ref']['line_video_name']
        damage_time_sec = entry['damage_ref']['damage_time_ms_ref']  # Corrected variable name
        output_folder = os.path.join(output_base_folder, os.path.splitext(video_name)[0])
        os.makedirs(output_folder, exist_ok=True)

        # Find corresponding video file
        video_file_path = None
        for root, dirs, files in os.walk(video_folder):
            for file in files:
                if file.startswith(video_name.split('___')[0]):
                    video_file_path = os.path.join(root, file)
                    break
            if video_file_path:
                break

        if video_file_path:
            # Extract frames from (t-2) sec to (t+2) sec
            start_time = max(0, damage_time_sec - 2)
            end_time = damage_time_sec + 2

            # Extract frames
            extract_frames(video_file_path, output_folder, start_time, end_time)

if __name__ == "__main__":
    main()
