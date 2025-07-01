import os
import tkinter as tk
from tkinter import filedialog

def traverse_directories(root_dir):
    """
    Recursively traverse all directories starting from root_dir
    and print their paths.
    """
    for dirpath, dirnames, filenames in os.walk(root_dir):
        print(f"Directory: {dirpath}")
        for dirname in dirnames:
            print(f"  Subdirectory: {os.path.join(dirpath, dirname)}")
        for filename in filenames:
            print(f"  File: {os.path.join(dirpath, filename)}")

if __name__ == "__main__":
    # Hide the main Tk window
    root = tk.Tk()
    root.withdraw()

    # Open the folder selection dialog
    root_directory = filedialog.askdirectory(title="Select a Root Directory")

    if root_directory:
        print(f"\nTraversing directories under: {root_directory}\n")
        traverse_directories(root_directory)
    else:
        print("No directory selected.")
