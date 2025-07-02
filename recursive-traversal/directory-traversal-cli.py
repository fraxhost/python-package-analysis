import os

def traverse_directories(root_dir):
    count = 0
    """
    Recursively traverse all directories starting from root_dir
    and print their paths.`
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")
        
        """ Traverse all directories """
        for dirname in dirnames:
            print(f"  Subdirectory: {os.path.join(dirpath, dirname)}")
        
        """ Traverse all files """
        for filename in filenames:
            print(f"  File: {os.path.join(dirpath, filename)}")


if __name__ == "__main__":
    root_directory = input("Enter the path to the root directory: ").strip()
    if os.path.isdir(root_directory):
        traverse_directories(root_directory)
    else:
        print(f"Error: '{root_directory}' is not a valid directory.")
