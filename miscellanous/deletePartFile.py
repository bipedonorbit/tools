import os
import re

def list_files(directory):
    print("""
               
file detected
              
""")
    file_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_paths.append(os.path.join(root, file))

    return file_paths

def delete_part_files(folder_path, pattern):
    

    files = list_files(folder_path)
    partFiles=[]

    print("""
               
part files detected
              
""")
    for file in files:
        if re.search(pattern, file):
            partFiles.append(file)
            print (file)
    if partFiles:
        confirm = input(f"Delete ? (y/n): ").strip().lower()
        if confirm == 'y':
            for file in files:
                file_path = os.path.join(folder_path, file)
                
                # Check if the file matches the pattern
                if re.search(pattern, file):
                    try:
                        # Delete the file
                        os.remove(file_path)
                        print(f"Deleted: {file}")
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")
        else:
            print(f"Not deleting files")
    else:
        print(f"No part file")



folder_path=r"\\MINERVA\3d4_23_24\MECHA\08_editing\input\05_render"

delete_part_files(folder_path, "_part")
