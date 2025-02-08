import cv2
import os
import sys
from PySide6.QtWidgets import *
import imageio
from PIL import Image

def open_Explorer_for_folder(default_folder):
    """
    this function open a file explorer and return the path of the selected folder
    """
    app = QApplication(sys.argv)
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly 
    folder_path,_ = QFileDialog.getOpenFileNames(None, "Select Files", default_folder, "All Files (*)", options=options)
    return folder_path

def convert_video_to_gif(input_video_path, output_gif_path, fps=10,maxHeight=512):
    print("converting "+input_video_path)
    
    # Read video frames using imageio
    video_reader = imageio.get_reader(input_video_path)
    frames = [Image.fromarray(frame) for frame in video_reader]

    # Set the frames per second for the GIF
    duration = 1 / fps
    for i, frame in enumerate(frames):
        aspect_ratio = frame.width / frame.height
        new_height = min(frame.height, maxHeight)
        new_width = int(aspect_ratio * new_height)
        frames[i] = frame.resize((new_width, new_height), Image.LANCZOS)
    # Save the frames as a GIF using Pillow
    frames[0].save(output_gif_path, save_all=True, append_images=frames[1:], duration=duration, loop=0)
    


default_folder=r"S:\ressource\video\comp footage\cartoon\CinePacks Glow FX 2.1\Accents"

folderPath=open_Explorer_for_folder(default_folder)

for videoPath in folderPath:
    filename, extension = os.path.splitext(videoPath)
    outputPath = filename + ".gif"

    convert_video_to_gif(videoPath, outputPath, fps=10)
    print("done!")
print("finished!")