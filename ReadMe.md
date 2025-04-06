# Subtitle Renamer For Plex

This program rename the subtitle files so Plex can recognized the language assossiated to the video.
If you have multiple files with the same language, you can manually choose which one you want to keep and delete the other to be sure to keep the right one or this program will increment a number at the end. Plex may not recognized all files.

The program will ask you two arguments. The path and the video name. Please keep the video name blank if the subtitile file name already contains the name of the video. Or you can pass the Path and video name in argument from the console.


### Download and install
```
git clone git@github.com:Bradford1138/SubtitleRenamerForPlex.git
cd SubtitleRenamerForPlex
pip install -r requirements.txt
```

### Examples
Example of subtitle files with the name of the video: \
![alt text](ReadMeMedia/Before_with_name.JPG "Before_with_name")
![alt text](ReadMeMedia/Console_with_name.JPG "Console_with_name")
![alt text](ReadMeMedia/After.JPG "After")
\
\
Example of subtitle files without the name of the video: \
![alt text](ReadMeMedia/Before_without_name.JPG "Before_without_name")
![alt text](ReadMeMedia/Console_without_name.JPG "Console_without_name")
![alt text](ReadMeMedia/After.JPG "After")

Note: the script "SubtitleRenamerForPlex.py" can be called with parameters: 
1. Directory path
2. Episode file name (Without extension)
3. Bypass exit message (Optional, default "False")

### By Season

If multiple sub folders need to be looped in and the episode name have the same name as the sub folder, the script "BySeason.py" can be used. Episode file can even be in the parent folder. i.e. \
Before: \
![alt text](ReadMeMedia/Season_folder_before.JPG "Before by season") \
Running script: \
![alt text](ReadMeMedia/Season_folder_script.JPG "By season script") \
After: \
![alt text](ReadMeMedia/Season_folder_after.JPG "After by season") 

