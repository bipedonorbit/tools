import sys
import os
import json
import cv2
from pytube import YouTube

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

output_path = r"C:\Users\l.bonnaud\Music\TheZone"
chrome_shortcuts=[]

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle("Multiple Buttons Example")
        self.setGeometry(100, 100, 400, 400)  # Set window position and size
        self.setMinimumSize(QSize(400, 400))

        policy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        policy.setHorizontalStretch(0)
        policy.setVerticalStretch(0)

        # Create a QWidget to hold the layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Create a QVBoxLayout to hold the buttons
        layout = QVBoxLayout(self.central_widget)

        # Create buttons and add them to the main window
        self.button1 = QPushButton("add fcount and name to videos", self)
        """self.button1.setSizePolicy(policy)"""
        self.button1.setFocusPolicy(Qt.NoFocus)
        self.button1.setMinimumSize(QSize(0, 50))

        self.button2 = QPushButton("download music from youtube links", self)
        """self.button2.setSizePolicy(policy)"""
        self.button2.setFocusPolicy(Qt.NoFocus)
        self.button2.setMinimumSize(QSize(0, 50))

        self.button3 = QPushButton("mirror images selected", self)
        """self.button3.setSizePolicy(policy)"""
        self.button3.setFocusPolicy(Qt.NoFocus)
        self.button3.setMinimumSize(QSize(0, 50))



        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)

        # Connect button click signals to functions
        self.button1.clicked.connect(self.button1_clicked)
        self.button2.clicked.connect(self.button2_clicked)
        self.button3.clicked.connect(self.button3_clicked)

    def button1_clicked(self):
        add_fcount_and_name_to_video()

    def button2_clicked(self):
        open_explorer_and_get_paths()

    def button3_clicked(self):
        open_explorer_and_get_paths_mirror()


def high_lighted_text(input_image,text,x,y,font_scale):
    # Set the font scale and thickness for the border
    font_scale = 1
    font_thickness = 2
    border_thickness = 5
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_color = (255, 255, 255)
    hilight_color = (0, 0, 0)

    # Get the size of the text
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)

    # Calculate the position for the border
    x1 = x - border_thickness
    y1 = y - border_thickness-text_size[1]
    x2 = x + text_size[0] + border_thickness
    y2 = y + text_size[1] + border_thickness-text_size[1]

    # Draw the black border
    cv2.rectangle(input_image, (x1, y1), (x2, y2), hilight_color, -1)  # -1 fills the rectangle
    cv2.putText(input_image, text, (x, y), font, font_scale, text_color, font_thickness)


def check_if_path_exist(path):
    if os.path.exists(path):
        print(f"The path '{path}' exists.")
    else:
        print(f"The path '{path}' does not exist.")


def add_name_and_frame_count_to_video(file_input):
    print("starting with"+file_input)
    check_if_path_exist(file_input)

    directory_path=os.path.dirname(file_input)
    basename=os.path.basename(file_input)
    filename=os.path.splitext(basename)[0]
    extension=os.path.splitext(basename)[1]

    file_output=os.path.join(directory_path, filename +"_com"+ extension)

    print("creation of "+file_output)

    # Ouvrir la vidéo d'entrée
    input_video = cv2.VideoCapture(file_input)
    print(input_video)

    # Récupérer les propriétés de la vidéo (taille, framerate, etc.)
    frame_width = int(input_video.get(3))
    frame_height = int(input_video.get(4))
    fps = int(input_video.get(5))


    # Créer un objet VideoWriter pour écrire la vidéo de sortie
    output_video = cv2.VideoWriter(file_output, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    # Boucle à travers chaque frame de la vidéo
    frame_count = 1
    while True:
        ret, frame = input_video.read()
        if not ret:
            break
        high_lighted_text(frame,filename,50,50,1)
        frame_counter="f "+str(frame_count)
        high_lighted_text(frame,frame_counter,50,100,1)
        output_video.write(frame)
        print(frame_counter)
        frame_count+=1

    # Fermer les objets de vidéo
    input_video.release()
    output_video.release()

    # Fermer toutes les fenêtres OpenCV
    cv2.destroyAllWindows()
    print("finished !")


def add_fcount_and_name_to_video():

    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Allow selecting read-only files
    files, _ = QFileDialog.getOpenFileNames(None,"Select Files","","All Files (*);;Text Files (*.txt);;Python Files (*.py)",options=options,)

    if files:
        print("Selected Files:")
        for file in files:
            print(file)
            add_name_and_frame_count_to_video(file)
        

def download_mp3_from_link(link, output_path):
    if link.startswith("http://") or link.startswith("https://"):
        print("Downloading..."+link)
        yt = YouTube(link)
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream:
            out_file =audio_stream.download(output_path)

            # save the file
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)

            print("Download complete.")

        else:
            print("pas d'audio disponible")
    else:
        print("its not a chrome link !")


def open_explorer_and_get_paths():
    
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Allow read-only access
    files, _ = QFileDialog.getOpenFileNames(None,"Select File","","All Files (*)",options=options)
    for file in files:
        if file:
            print("Selected Files:")
            for file in files:
                chrome_shortcuts.append(file)

            print(chrome_shortcuts)
            QApplication.exit()

            for shortcut in chrome_shortcuts:
                download_mp3_from_link(shortcut,output_path)


def open_explorer_and_get_paths_mirror():
    
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Allow read-only access
    files, _ = QFileDialog.getOpenFileNames(None,"Select File","","All Files (*)",options=options)
    for file in files:
        print("fliping "+file)
        image = cv2.imread(file)
        imagemirrored=cv2.flip(image, 1)
        cv2.imwrite(file,imagemirrored)







def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


