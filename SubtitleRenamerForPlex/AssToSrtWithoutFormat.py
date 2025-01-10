import os
from pathlib import Path
import re

def convert_ass_to_srt(ass_file):
    srt_file = os.path.join(os.path.dirname(ass_file), os.path.splitext(os.path.basename(ass_file))[0] + ".srt")
    try:
        with open(ass_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Find the start of the dialogue section
        dialogue_start = False
        dialogues = []
        for line in lines:
            if line.strip().startswith("[Events]"):
                dialogue_start = True
            elif dialogue_start and line.strip().startswith("Dialogue:"):
                dialogues.append(line)

        srt_lines = []
        index = 1
        for dialogue in dialogues:
            # Split dialogue line into fields
            fields = dialogue.split(",", 9)
            if len(fields) < 10:
                continue

            start_time = convert_time(fields[1])
            end_time = convert_time(fields[2])
            text = remove_formatting(fields[9])

            srt_lines.append(f"{index}")
            srt_lines.append(f"{start_time} --> {end_time}")
            srt_lines.append(text)
            srt_lines.append("")
            index += 1

        with open(srt_file, 'w', encoding='utf-8') as file:
            file.write("\n".join(srt_lines))

        print(f"Conversion complete! Saved as {srt_file}")

    except Exception as e:
        print(f"An error occurred: {e}")
        raise

def convert_time(ass_time):
    """Convert ASS time format (h:mm:ss.cs) to SRT time format (hh:mm:ss,ms)"""
    match = re.match(r"(\d+):(\d{2}):(\d{2})\.(\d{2})", ass_time)
    if match:
        hours, minutes, seconds, centiseconds = match.groups()
        milliseconds = int(centiseconds) * 10
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02},{milliseconds:03}"
    return "00:00:00,000"

def remove_formatting(text):
    """Remove ASS formatting tags from text"""
    # Remove inline override tags (e.g., {\i1}, {\pos(400,300)})
    text = re.sub(r"\{.*?\}", "", text)
    # Replace escaped commas with regular commas
    text = text.replace("\\N", "\n").replace("\\n", "\n")
    return text.strip()


root = input("Enter directory path (i.e. C:/myfolder/Season1): ")

for sub_file in os.listdir(root):
    convert_ass_to_srt(os.path.join(root, sub_file))

# H:/subs