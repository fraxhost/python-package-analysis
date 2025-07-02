import os
import tkinter as tk
from tkinter import filedialog, messagebox

def count_immediate_subdirs(path):
    """Count only the immediate subdirectories directly inside the given path."""
    try:
        return sum(1 for entry in os.scandir(path) if entry.is_dir())
    except PermissionError:
        print(f"Permission denied: {path}")
        return 0

def select_directory_and_count():
    """Open a folder picker, count immediate subdirectories, and show the result."""
    root_dir = filedialog.askdirectory(title="Select Directory to Count Immediate Subdirectories")
    if root_dir:
        count = count_immediate_subdirs(root_dir)
        messagebox.showinfo("Immediate Subdirectory Count",
                            f"Directory:\n{root_dir}\n\nImmediate subdirectories found: {count}")
    else:
        messagebox.showwarning("No Directory Selected", "Please select a directory.")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main Tk window

    select_directory_and_count()
