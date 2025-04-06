import os
from pathlib import Path
import re

root = "H:/VM shared drive/tv/Stargate SG1 Season 1 -10 (1997–2007) HEVC [720p-AAC 5.1] (8.4)/Stargate SG-1 Season 09/SubBackup"

#for file in os.listdir(root):
#    print(file)




# Define the folder containing the files
folder = "H:/S01"  # Change this to your actual folder path

# Get list of video and subtitle files
video_files = [f for f in os.listdir(folder) if f.endswith((".mp4", ".mkv", ".avi", ".mov"))]
subtitle_files = [f for f in os.listdir(folder) if f.endswith(".srt")]

# Regex to extract episode number
pattern = re.compile(r"S(\d+)E(\d+)")

# Create a mapping of episode numbers to video filenames
video_map = {}
for video in video_files:
    match = pattern.search(video)
    if match:
        season, episode = match.groups()
        video_map[(season, episode)] = video

# Rename subtitle files to match the corresponding video files
for subtitle in subtitle_files:
    match = pattern.search(subtitle)
    if match:
        season, episode = match.groups()
        if (season, episode) in video_map:
            new_name = os.path.splitext(video_map[(season, episode)])[0] + ".srt"
            old_path = os.path.join(folder, subtitle)
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed: {subtitle} -> {new_name}")

print("Renaming complete.")
