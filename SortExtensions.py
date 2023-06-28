import os
import shutil

audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def organize_files(directory_path, folder_type, folder_name):
    # Change the current working directory
    os.chdir(directory_path)

    for file in os.listdir():
        if is_image(file) and folder_type == "i":
            destination_folder = os.path.join(directory_path, folder_name)
        elif is_video(file) and folder_type == "v":
            destination_folder = os.path.join(directory_path, folder_name)
        elif is_audio(file) and folder_type == "a":
            destination_folder = os.path.join(directory_path, folder_name)
        else:
            continue  # Skip files that don't match the selected folder type

        # Create the destination folder if it doesn't exist
        os.makedirs(destination_folder, exist_ok=True)

        # Move the file to the destination folder
        shutil.move(file, destination_folder)

# Accept the directory path from the user
directory_path = input("Enter the directory path: ")

# Ask the user whether they want to create a new folder or use an existing folder
create_new_folder = input("Do you want to create a new folder? (yes/no): ")

if create_new_folder.lower() == "yes":
    # Ask the user which folder to create
    print("Choose a folder type:")
    print("a - Audio")
    print("v - Video")
    print("i - Images")
    folder_type = input("Enter the folder type: ")

    # Prompt for the folder name based on the selected folder type
    folder_name = input("Enter the folder name: ")

    # Call the function to organize the files into the selected folder
    organize_files(directory_path, folder_type, folder_name)
else:
    # Ask the user for the existing folder name
    folder_name = input("Enter the existing folder name: ")

    # Ask the user which folder to create
    print("Choose a folder type:")
    print("a - Audio")
    print("v - Video")
    print("i - Images")
    folder_type = input("What type of folder is it: ")

    # Call the function to organize the files into the selected folder
    organize_files(directory_path, folder_type, folder_name)

    # Call the function to organize the files
