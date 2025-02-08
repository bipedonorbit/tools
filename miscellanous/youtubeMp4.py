import os
import sys

from pytube import YouTube
from PySide6.QtWidgets import * 

output_path = r"C:\Users\l.bonnaud\Music\TheZone"
chrome_shortcuts=[]

def download_mp4_from_link(link, output_path):
    if link.startswith("http://") or link.startswith("https://"):
        print("Downloading..."+link)
        yt = YouTube(link)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
        if stream:
            try:
                out_file =stream.download(output_path)
                # save the file
                #base, ext = os.path.splitext(out_file)
                #new_file = base + '.mp4'
                #os.rename(out_file, new_file)
                print("Download complete.")
                
            except Exception as e:
                print("An error occurred:", e)
            
        else:
            print("pas d'audio disponible")
    else:
        print("its not a chrome link !")


def open_explorer_and_get_paths():
    app = QApplication(sys.argv)
    options = QFileDialog.Options()
    options |= QFileDialog.ReadOnly  # Allow read-only access
    files, _ = QFileDialog.getOpenFileNames(None,"Select File","","All Files (*)",options=options)
    for file in files:
        if file:
            print("Selected Files:")
            for file in files:
                chrome_shortcuts.append(file)

            print(chrome_shortcuts)
            

            for shortcut in chrome_shortcuts:
                download_mp4_from_link(shortcut,output_path)
            QApplication.exit()


open_explorer_and_get_paths()


print("finished")