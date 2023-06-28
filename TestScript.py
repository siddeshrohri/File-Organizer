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

def create_folder(directory_path, folder_name):
    # Create the folder if it doesn't exist
    folder_path = os.path.join(directory_path, folder_name)
    os.makedirs(folder_path, exist_ok=True)
    return folder_path

def move_file(source_file, destination_folder):
    # Move the file to the destination folder
    shutil.move(source_file, destination_folder)

def organize_files(directory_path, folder_type, folder_name):
    # Change the current working directory
    os.chdir(directory_path)

    for file in os.listdir():
        if is_image(file) and folder_type == "i":
            destination_folder = create_folder(directory_path, folder_name)
            move_file(file, destination_folder)
        elif is_video(file) and folder_type == "v":
            destination_folder = create_folder(directory_path, folder_name)
            move_file(file, destination_folder)
        elif is_audio(file) and folder_type == "a":
            destination_folder = create_folder(directory_path, folder_name)
            move_file(file, destination_folder)
        else:
            continue  # Skip files that don't match the selected folder type

# Test case 1: Create a new folder for images
def test_create_new_folder_images():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "i"
    folder_name = "Images"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that the Images folder is created
    assert os.path.exists(os.path.join(directory_path, folder_name))
    
    # Assert that image files are moved to the Images folder
    for file in os.listdir(directory_path):
        if is_image(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Test case 2: Create a new folder for videos
def test_create_new_folder_videos():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "v"
    folder_name = "Videos"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that the Videos folder is created
    assert os.path.exists(os.path.join(directory_path, folder_name))
    
    # Assert that video files are moved to the Videos folder
    for file in os.listdir(directory_path):
        if is_video(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Test case 3: Create a new folder for audio
def test_create_new_folder_audio():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "a"
    folder_name = "Audio"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that the Audio folder is created
    assert os.path.exists(os.path.join(directory_path, folder_name))
    
    # Assert that audio files are moved to the Audio folder
    for file in os.listdir(directory_path):
        if is_audio(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Test case 4: Use an existing folder for images
def test_use_existing_folder_images():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "i"
    folder_name = "ExistingImages"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that image files are moved to the existing Images folder
    for file in os.listdir(directory_path):
        if is_image(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Test case 5: Use an existing folder for videos
def test_use_existing_folder_videos():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "v"
    folder_name = "ExistingVideos"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that video files are moved to the existing Videos folder
    for file in os.listdir(directory_path):
        if is_video(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Test case 6: Use an existing folder for audio
def test_use_existing_folder_audio():
    directory_path = r"C:\Users\sidde\Desktop\Test"
    folder_type = "a"
    folder_name = "ExistingAudio"
    
    organize_files(directory_path, folder_type, folder_name)
    
    # Assert that audio files are moved to the existing Audio folder
    for file in os.listdir(directory_path):
        if is_audio(file):
            assert os.path.exists(os.path.join(directory_path, folder_name, file))

# Run the test cases if the user chooses to run the test script
def run_test_script():
    print("Test Script")
    print("-" * 50)
    print("This script will test the functionality of the file organizer.")
    print("Running the test cases...\n")
    
    test_create_new_folder_images()
    test_create_new_folder_videos()
    test_create_new_folder_audio()
    test_use_existing_folder_images()
    test_use_existing_folder_videos()
    test_use_existing_folder_audio()
    
    print("\nAll tests passed successfully.")

# Prompt the user to run the test script
def prompt_to_run_test_script():
    run_tests = input("Do you want to run the test script? (yes/no): ")
    
    if run_tests.lower() == "yes":
        run_test_script()
    else:
        print("Test script not run.")

prompt_to_run_test_script()
