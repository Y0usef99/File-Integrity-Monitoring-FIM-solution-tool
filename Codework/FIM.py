import os
import shutil
import hashlib
import time

# set the directory to be monitored
#directory_to_watch = '/path/to/your/directory'
directory_to_watch = 'E:\ITI\python'
# set the log file path
#log_file_path = '/path/to/your/logfile.txt'
log_file_path = 'E:\ITI\python\logfile.txt'
#source_directory = '/path/to/source_directory'
source_directory = 'E:\ITI\python'
#destination_directory = '/path/to/destination_directory'
destination_directory = 'E:\ITI\python2'
tim = {}

# Normal Mode
def normal():

    # infinite loop to monitor for changes
    while True:
        # create an initial list of files in the directory
        files_in_directory = os.listdir(directory_to_watch)
        for file in files_in_directory:
            tim[file] = os.path.getmtime(os.path.join(directory_to_watch, file))
        # wait for 60 seconds
        time.sleep(60)
        print("60 Seconds Elapsed...")
        # get the current list of files in the directory
        current_files_in_directory = os.listdir(directory_to_watch)

        # check for new files
        new_files = set(current_files_in_directory) - set(files_in_directory)
        for file in new_files:
            print(f'New file added: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'New file added: {file}\n')

        # check for deleted files
        deleted_files = set(files_in_directory) - set(current_files_in_directory)
        for file in deleted_files:
            print(f'File deleted: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'File deleted: {file}\n')

        # check for modified files
        modified_files = set()
        for file in current_files_in_directory:
            if file in files_in_directory:
                if os.path.getmtime(os.path.join(directory_to_watch, file)) > tim[file]:
                    modified_files.add(file)
        for file in modified_files:
            print(f'File modified: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'File modified: {file}\n')
    

# Aggressive Mode

def get_file_md5(file_path):
    """
    Returns the MD5 hash of the specified file.
    """
    with open(file_path, 'rb') as f:
        hash_md5 = hashlib.md5()
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def mirror_directory(source, destination):
    """
    Mirrors a directory hierarchy from the source directory to the destination directory,
    renaming files with the content md5 of the original file data.
    """
    for root, dirs, files in os.walk(source):
        # Create the destination directory if it doesn't exist
        destination_dir = root.replace(source, destination)
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Copy each file to the destination directory and rename it with the md5 hash
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(destination_dir, get_file_md5(source_file))
            shutil.copy2(source_file, destination_file)

def aggressive():
    # infinite loop to monitor for changes
    while True:
        # create an initial list of files in the directory
        files_in_directory = os.listdir(directory_to_watch)
        for file in files_in_directory:
            tim[file] = os.path.getmtime(os.path.join(directory_to_watch, file))

        # Create a new mirror copy if any file is modified
        mirror_directory(source_directory, destination_directory)
        # wait for 60 seconds
        time.sleep(60)
        print("60 Seconds Elapsed...Updating Mirror Directory")
        # get the current list of files in the directory
        current_files_in_directory = os.listdir(directory_to_watch)
        # check for new files
        new_files = set(current_files_in_directory) - set(files_in_directory)
        for file in new_files:
            print(f'New file added: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'New file added: {file}\n')
        # check for deleted files
        deleted_files = set(files_in_directory) - set(current_files_in_directory)
        for file in deleted_files:
            print(f'File deleted: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'File deleted: {file}\n')
        # check for modified files
        modified_files = set()
        for file in current_files_in_directory:
            if file in files_in_directory:
                if os.path.getmtime(os.path.join(directory_to_watch, file)) > tim[file]:
                    modified_files.add(file)
        for file in modified_files:
            print(f'File modified: {file}')
            with open(log_file_path, 'a') as log_file:
                log_file.write(f'File modified: {file}\n')



# Main
print("1- Normal Mode \n2- Aggressive Mode")

choice = int(input("Enter Choice: "))

if choice == 1:
    normal()
elif choice == 2:
    aggressive() 