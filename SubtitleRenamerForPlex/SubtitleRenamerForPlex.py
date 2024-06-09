from iso639 import Lang
from iso639 import exceptions
import os
from pathlib import Path
import re
import sys

sub_extensions = [".srt", ".ass", ".ssa", ".smi", ".vtt"]
validation_recommended = False

try:
    directory = sys.argv[1]
    video_name = sys.argv[2]
    bypass_exit_msg = sys.argv[3] or "False"
except IndexError:  #If no argument is passed, ask for parameters
    directory = input("Enter directory path (i.e. C:/myfolder/subs): ")
    video_name = input("Enter the movie/episode file name. Just tap the Enter key if the subtitle files already have the movie/episode name in the file name: ")
    bypass_exit_msg = "False"

#debug
#directory = "H:/rename/"
#video_name = "Star.Wars.Tales.of.the.Jedi.S01E01.1080p.WEBRip.x265-RARBG[eztv.re]"

if len(video_name) > 0:
    video_name = video_name + "."

for filename in filter(lambda f: f.endswith(tuple(sub_extensions)), os.listdir(directory)):
    filename_incr = 1   #Initialize increment in case there is multiple file with the same language
    lastDotIdx = Path(filename).stem.rfind(".") #Get the index of the last dot before the language
    filename_1 = filename[:lastDotIdx + 1]  #First part of the file name to keep
    
    try:
        #Greek have two ISO-639-2 codes, Modern(gre) and Ancient(grc)
        if re.sub("[0-9]+_", "", Path(filename[lastDotIdx+1:]).stem) == "Greek":
            lg = "gre"
        else:
            lg = Lang(re.sub("[0-9]+_", "", Path(filename[lastDotIdx+1:]).stem)).pt2b

        new_filename = video_name + filename_1 + lg + Path(filename).suffix
        while os.path.isfile(os.path.join(directory, new_filename)): #If the new file name already exists, add a number at the end
            new_filename = video_name + filename_1 + lg + "." + str(filename_incr) + Path(filename).suffix
            filename_incr += 1
            validation_recommended = True

        os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
    except  exceptions.InvalidLanguageValue:
        print("Only valid ISO 639 language values are supported as arguments. Language not found: " + re.sub("[0-9]+_", "", Path(filename[lastDotIdx+1:]).stem))

if validation_recommended == True:
    print("Please validate the subtitles, there may be multiple files with the same language. Plex may not recognized them all.")

if bypass_exit_msg == "False":
    input("Press Enter to exit")
    