import cv2
import os
import sys
from PySide6.QtWidgets import *

extention=".png"

def check_if_path_exist(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
    else:
        print(f"The path '{path}' does not exist.")


def images_to_video(image_folder, video_path='output_video.mp4', fps=24):
    images = [img for img in os.listdir(image_folder) if img.endswith(extention)]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"mp4v"), fps, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()
    print("finished !")




frames_per_second = 24
app = QApplication(sys.argv)
options = QFileDialog.Options()
options |= QFileDialog.ReadOnly  # Allow selecting read-only files
folder_path = QFileDialog.getExistingDirectory(None, "Select Folder", options=options)

output_video_name = os.path.join(folder_path,"ouput.mp4")


if folder_path:
    print(f"folder_path:{folder_path}")
    images_to_video(folder_path,output_video_name, frames_per_second)
        

QApplication.exit()



