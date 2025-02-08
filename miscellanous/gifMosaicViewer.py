import cv2
import os
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import QSize
import imageio
from PIL import Image

def open_Explorer_for_folder(default_folder):
    """
    this function open a file explorer and return the path of the selected folder
    """
    app = QApplication(sys.argv)
    if app is None:
        app = QApplication(sys.argv)
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly 
    folder_path,_ = QFileDialog.getOpenFileNames(None, "Select Files", default_folder, "All Files (*)", options=options)

    return folder_path


class GifWindow(QMainWindow):
    def __init__(self, gifs):
        super().__init__()

        self.setWindowTitle("GIF Viewer")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        

        layout = QVBoxLayout(central_widget)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        content_widget = QWidget(scroll_area)
        content_layout = QVBoxLayout(content_widget)

        for gif_path in gifs:
            max_width = 500
            max_height = 300
            
            gif_label_title = QLabel("self")
            gif_label = QLabel(self)
            gif_label.setMaximumSize(max_width, max_height)

            gif_movie = QMovie(gif_path)
            gif_movie.setScaledSize(QSize(max_width, max_height))  # Resize the GIF
            gif_label.setMovie(gif_movie)
            gif_movie.start()

            layout.addWidget(gif_label)
            layout.addWidget(gif_label_title)

        self.show()

if __name__ == "__main__":
    default_folder=r"S:\ressource\video\comp footage\cartoon\CinePacks Glow FX 2.1\Accents"
    folderPath=open_Explorer_for_folder(default_folder)



    # Replace the paths with the actual paths of your GIFs

    window = GifWindow(folderPath)

    sys.exit(QApplication.instance().exec())

    

