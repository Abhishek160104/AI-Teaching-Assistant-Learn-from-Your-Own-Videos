## Coverting video to mp3
import os
import subprocess

file = os.listdir("Video")
for file in file:
    print(file)
    tutorial_number = file.split(" [")[0].split(" #")[1]
    file_name = file.split(" [")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg", "-i", f"Video/{file}", f"Audio/{tutorial_number} - {file_name}.mp3"])
