import os

def count_immediate_subdirs(path):
    """Count only the immediate subdirectories directly inside the given path."""
    try:
        return sum(1 for entry in os.scandir(path) if entry.is_dir())
    except PermissionError:
        print(f"Permission denied: {path}")
        return 0

if __name__ == "__main__":
    root = input("Enter the path to the root directory: ").strip()
    if os.path.isdir(root):
        count = count_immediate_subdirs(root)
        print(f"Immediate subdirectories found: {count}")
    else:
        print(f"Error: '{root}' is not a valid directory.")
