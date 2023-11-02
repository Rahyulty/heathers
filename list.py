import os

def print_file_names_in_folder(folder_name):
    # Get the current directory path
    current_directory = os.path.dirname(__file__)

    # Iterate through the files in the current directory
    for root, dirs, files in os.walk(current_directory):
        for dir in dirs:
            # Check if the current directory matches the given folder name
            if dir == folder_name:
                folder_path = os.path.join(root, dir)
                # List all files in the specified folder
                folder_files = os.listdir(folder_path)
                for file in folder_files:
                    print(file)

# Replace 'YourFolderName' with the name of the folder you want to list the files from
folder_name = 'sound'
print(f"Files in folder '{folder_name}':")
print_file_names_in_folder(folder_name)
