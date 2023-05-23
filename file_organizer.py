# FILE ORGANIZER
'''
    #? Instructions:
        1. Check the imports and install the missing ones
        2. Delete any folder from folders[] that you dont need otherwise all will be created
        3. Run the code : python file_organizer.py "{folder-name or path}"
        4. Wait for the execution
        5. Check the folder
'''

import os           #? pip install os
import shutil       #? pip install shutil
import argparse     #? pip install argparse

def _file_organizer(directory):
    #? Gets all the files in the specified directory
    files = os.listdir(directory)

    #? Folders for each type of file
    folders = {
        'Images': ['jpg', 'jpeg', 'png', 'gif', 'ico', 'svg', 'bmp'],
        'Documents': ['doc', 'docx', 'txt', 'pdf', 'xls', 'xlsx', 'ppt', 'pptx', 'csv', 'odt', 'ods', 'odp', 'odg', 'odf', 'rtf', 'tex', 'wpd'],
        'Videos': ['mp4', 'avi', 'mov', 'flv', 'wmv', 'mkv', 'webm', 'mpg', 'mpeg', '3gp'],
        'Music': ['mp3', 'wav', 'ogg', 'm4a', 'flac', 'aac'],
        'Archives': ['zip', 'rar', '7z', 'tar', 'gz', 'pkg', 'deb'],
        'Programs': ['exe', 'msi', 'apk', 'jar', 'bat', 'sh'],
        'Others': []
    }

    #? Create the folders if they don't exist
    for folder_name in folders:
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    #? Moving the files to their respective folders
    for file in files:
        if file != __file__:  #! Ignores this file
            file_extension = file.split('.')[-1].lower()  #? Gets the file extension

            #? Determines the destination folder
            destination_folder = ''
            for folder_name, extensions in folders.items():
                if file_extension in extensions:
                    destination_folder = folder_name
                    break
            if not destination_folder:
                destination_folder = 'Others'

            #? Moves the file to the destination folder
            source_path = os.path.join(directory, file)
            destination_path = os.path.join(directory, destination_folder, file)
            shutil.move(source_path, destination_path)

            #? Prints the file and the destination folder
            print(f"Moved '{file}' to '{destination_folder}' folder.")

def __main():
    parser = argparse.ArgumentParser(description='Joao')
    parser.add_argument('directory', type=str, help='Path to the directory to organize')
    args = parser.parse_args()

    # Get the current working directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Combine the current directory with the provided directory path
    directory_path = os.path.join(current_dir, args.directory)
    _file_organizer(directory_path)


__main()