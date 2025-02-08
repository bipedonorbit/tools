import os
import shutil
from datetime import datetime
from pathlib import Path

def get_week_folder(mod_time):
    year, week, _ = mod_time.isocalendar()
    return f"{year}_Week_{week}"

def scan_and_sort_by_week(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            
            mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            print(os.path.getmtime(file_path))
            week_folder = get_week_folder(mod_time)
            week_folder_path = os.path.join(destination_folder, week_folder)

            if not os.path.exists(week_folder_path):
                os.makedirs(week_folder_path)

            dest_file_path = os.path.join(week_folder_path, file)
            shutil.move(file_path, dest_file_path)


source_folder = r"A:\Archives\9_cours_esma_esma_3D4_2023_2024\archive source productionV2"
destination_folder = r"A:\Archives\9_cours_esma_esma_3D4_2023_2024\archive source productionV2"
scan_and_sort_by_week(source_folder, destination_folder)
print("Files have been sorted by week.")
