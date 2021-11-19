import shutil
import os

files_directory = r'C:\\xpdf\\files\\'
software_directory = r'C:\\xpdf\\'


for directory in os.scandir(files_directory):
    if directory.is_dir():
        # shutil.move(entry.path, dst)
        print(directory)
        for files in os.scandir(directory):
            if files.is_file():
                print(files)
                shutil.move(files, files_directory)
                print(f'finished Move')