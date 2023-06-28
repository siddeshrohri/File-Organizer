File Organizer Script
This script allows you to organize files in a specified directory based on their file types. It helps you to categorize audio, video, and image files into separate folders.

Prerequisites
Python 3.x installed on your machine.
Getting Started
Clone or download the script to your local machine.

Open a terminal or command prompt and navigate to the directory where the script is located.

Run the script by executing the following command:

Copy code
python SortExtensions.py
Usage
Enter the directory path where the files are located when prompted.

Choose whether you want to create a new folder or use an existing folder:

If you choose to create a new folder:

Enter the folder type (a - Audio, v - Video, i - Images).
Enter the folder name.
If you choose to use an existing folder:

Enter the existing folder name.
Enter the folder type (a - Audio, v - Video, i - Images).
The script will organize the files into the selected folder based on their file types.

Supported File Types
The script supports the following file types:

Audio: .3ga, .aac, .ac3, .aif, .aiff, .alac, .amr, .ape, .au, .dss, .flac, .flv, .m4a, .m4b, .m4p, .mp3, .mpga, .ogg, .oga, .mogg, .opus, .qcp, .tta, .voc, .wav, .wma, .wv

Video: .webm, .MTS, .M2TS, .TS, .mov, .mp4, .m4p, .m4v, .mxf

Image: .jpg, .jpeg, .jfif, .pjpeg, .pjp, .png, .gif, .webp, .svg, .apng, .avif

Note
The script will create the destination folders if they don't already exist.

Files that don't match the selected folder type will be skipped and remain in the original directory.

Please ensure you have the necessary permissions to read the files and write/move files in the specified directory.

It is recommended to make a backup of your files before running the script.

License
This script is released under the MIT License. See the LICENSE file for more details.

Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create an issue or submit a pull request.

Contact
If you have any questions or need further assistance, feel free to contact.