import os
from pytube import YouTube

shortcut_folder= r"S:\ressource\code\ytmp3\liens"

def extract_url_from_chrome_shortcut(shortcut_path):
    try:
        items = os.listdir(shortcut_folder)
        with open(shortcut_path, 'r') as shortcut_file:
            for line in shortcut_file:
                if line.startswith('URL='):
                    return line[4:].strip()
    except Exception as e:
        print("An error occurred:", e)
    return None


def download_mp3_from_link(link,name):
    print("Downloading..."+name)
    yt = YouTube(link)
    audio_stream = yt.streams.filter(only_audio=True).first()
    if audio_stream:
        output_path = r"S:\ressource\code\ytmp3\output"
        audio_stream.download(output_path)
        print("Download complete.")
    else:
        print("pas d'audio disponible")
   
           
print("starting !")

for shortcut in os.listdir(shortcut_folder):
    shortcut_path=os.path.join(shortcut_folder, shortcut)
    link=extract_url_from_chrome_shortcut(shortcut_path)
    download_mp3_from_link(link,shortcut)
    os.remove(shortcut_path)

print("finished")