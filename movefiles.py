import os
import shutil


folder_name = 'images'


if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")


for file_name in os.listdir('.'):

    if file_name.endswith('.jpg'):

        shutil.move(file_name, folder_name)
        print(f"'{file_name}' has been moved to the '{folder_name}' folder.")