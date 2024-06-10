import os
from pathlib import Path

root = input("Enter directory path (i.e. C:/myfolder/Season1): ")

for file in os.listdir(root):
    if (os.path.isdir(os.path.join(root, file))):
        os.system("python SubtitleRenamerForPlex.py " + "\"" + os.path.join(root, file) + "\" \"" + file + "\" True")
    elif (os.path.exists(os.path.join(root, Path(file).stem)) and os.path.isdir(os.path.join(root, Path(file).stem))): #if the episode is outside the folder with his name, move the file inside the folder
        os.rename(os.path.join(root, file), os.path.join(root, Path(file).stem, file))

input("Press Enter to exit")