import os
from pathlib import Path

root = "H:\\SubRenamer\\WorkFolder"

for file in os.listdir(root):
    #print(file + " ; root: " + str(os.path.isdir(os.path.join(root, file))))
    
    if (os.path.isdir(os.path.join(root, file))):
        os.system("python SubtitleRenamerForPlex.py " + os.path.join(root, file) + " " + file + " True")
    elif (os.path.exists(os.path.join(root, Path(file).stem)) and os.path.isdir(os.path.join(root, Path(file).stem))): #if the episode is outside the folder with his name, move the file inse the folder
        os.rename(os.path.join(root, file), os.path.join(root, Path(file).stem, file))
