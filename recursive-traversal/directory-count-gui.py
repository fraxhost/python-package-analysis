import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_directories(path):
    """ Count all directories recursively starting from path. """
    count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        count += len(dirnames)
    return count

def select_directory_and_count():
    """ Open dialog to select a directory, count its subdirectories, and display result. """
    directory = filedialog.askdirectory(title="Select a directory to count subdirectories")
    if directory:
        dir_count = count_directories(directory)
        messagebox.showinfo("Directory Count", f"Total directories under:\n{directory}\n\nCount: {dir_count}")
    else:
        messagebox.showwarning("No Selection", "No directory was selected.")

if __name__ == "__main__":
    # Setup tkinter root
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Run directory selection and counting
    select_directory_and_count()
