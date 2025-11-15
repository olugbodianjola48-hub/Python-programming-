import sys
import os
import requests
import time

# Command Line Arguments (sys.argv)
# name = sys.argv[1]
# print("Hello,", name)
#
# # Join all arguments after the script name
# name = " ".join(sys.argv[1:])
# print("Hello,", name)

# to run file and pass arg - python greet.py Divine

# File Automation real world examples
# 1. Rename many documents or images at once
# Set the folder that contains the files you want to rename
folder_path = r'C:\Users\olugb\OneDrive\Desktop\Python Programming class\automation'

# Loop through each file in the folder
for count, filename in enumerate(os.listdir(folder_path)):
    new_name = f"assignment_{count + 1}.pdf"

    # Get the full path to the old and new files
    old_file = os.path.join(folder_path, filename)
    new_file = os.path.join(folder_path, new_name)

    # Rename the file
    os.rename(old_file, new_file)

print("All files renamed!")

# 2. Clean Up Old Files in a Folder
# Folder you want to clean
# folder = r'C:\Users\child\OneDrive\Desktop\My_Python_Projects\Python Class\pythonProject\ExampleAutomation'
#
# # Get the current time
# now = time.time()
#
# # Set how old a file must be to delete (in seconds)
# days = 30
# seconds_in_30_days = days * 86400  # 86400 seconds = 1 day
#
# # Loop through each file in the folder
# for file in os.listdir(folder):
#     file_path = os.path.join(folder, file)  # full path
#     if os.path.isfile(file_path):
#         file_age = now - os.path.getctime(file_path)
#         if file_age > seconds_in_30_days:
#             print(f"Found old file: {file}")
#             confirm = input("Delete it? (y/n): ").lower()
#             if confirm == "y":
#                 os.remove(file_path)
#                 print(f"Deleted: {file}")
