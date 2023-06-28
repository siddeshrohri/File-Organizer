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
    print(os.path.splitext(file)[1] in img)
    return os.path.splitext(file)[1] in img

def organize_files(directory_path, target_directory):
    # Change the current working directory
    os.chdir(directory_path)

    for file in os.listdir():
        if is_image(file):
            shutil.move(file, os.path.join(directory_path, target_directory, file))


# Accept the directory path from the user
directory_path = input("Enter the directory path: ")

# Ask the user if they want to create a new directory
create_new_directory = input("Do you want to create a new directory? (yes/no): ")
option = input("If you wish to create a directory, choose from the following options: a-Audio v-Video i-Image")
match option:
   case "a":
    if create_new_directory.lower() == "yes":
        # Accept the name of the new directory from the user
        new_directory_name = input("Enter the name of the new directory: ")
        new_directory_path = os.path.join(directory_path, new_directory_name)

        # Create the new directory
        os.makedirs(new_directory_path)

        # Call the outer function to organize the files in the new directory
        organize_files(directory_path, new_directory_name)
    else:
        # Accept the name of the existing directory from the user
        existing_directory_name = input("Enter the name of the existing directory: ")
        existing_directory_path = os.path.join(directory_path, existing_directory_name)

        # Call the outer function to organize the files in the existing directory
        organize_files(directory_path, existing_directory_name)
   
   case "v":
    if create_new_directory.lower() == "yes":
        # Accept the name of the new directory from the user
        new_directory_name = input("Enter the name of the new directory: ")
        new_directory_path = os.path.join(directory_path, new_directory_name)

        # Create the new directory
        os.makedirs(new_directory_path)

        # Call the outer function to organize the files in the new directory
        organize_files(directory_path, new_directory_name)
    else:
        # Accept the name of the existing directory from the user
        existing_directory_name = input("Enter the name of the existing directory: ")
        existing_directory_path = os.path.join(directory_path, existing_directory_name)

        # Call the outer function to organize the files in the existing directory
        organize_files(directory_path, existing_directory_name)

   case "i":
    if create_new_directory.lower() == "yes":
        # Accept the name of the new directory from the user
        new_directory_name = input("Enter the name of the new directory: ")
        new_directory_path = os.path.join(directory_path, new_directory_name)

        # Create the new directory
        os.makedirs(new_directory_path)

        # Call the outer function to organize the files in the new directory
        organize_files(directory_path, new_directory_name)
    else:
        # Accept the name of the existing directory from the user
        existing_directory_name = input("Enter the name of the existing directory: ")
        existing_directory_path = os.path.join(directory_path, existing_directory_name)

        # Call the outer function to organize the files in the existing directory
        organize_files(directory_path, existing_directory_name)

