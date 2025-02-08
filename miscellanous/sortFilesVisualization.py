import os
import csv
from datetime import datetime

def scan_and_sort_by_week(source_folder, output_csv):
    with open(output_csv, 'w', newline='') as csvfile:
        fieldnames = ['File', 'Size (MB)', 'Last Modified']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for root, _, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                size = os.path.getsize(file_path) / (1024 ** 2)
                size = round(size, 3)
                mod_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                writer.writerow({'File': file, 'Size (MB)': size, 'Last Modified': mod_time})

folder = r"A:\Archives\9_cours_esma_esma_3D4_2023_2024\archive source productionV2"
output_csv = r"A:\Archives\9_cours_esma_esma_3D4_2023_2024\archive source productionV2\file_info.csv"

scan_and_sort_by_week(folder, output_csv)
