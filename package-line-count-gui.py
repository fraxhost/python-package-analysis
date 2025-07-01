import os
import csv
import tkinter as tk
from tkinter import filedialog
import zipfile
import tarfile
import io

def count_lines_in_fileobj(fileobj):
    """Count lines from a file-like object."""
    return sum(1 for _ in fileobj)

def count_lines(filepath):
    """Count number of lines in a regular file."""
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(1 for _ in f)

def process_zip(zip_path, package_name, writer):
    """Process .zip archive and write .py files info to CSV."""
    try:
        with zipfile.ZipFile(zip_path) as z:
            py_files_found = False
            for info in z.infolist():
                if info.filename.endswith('.py') and not info.is_dir():
                    py_files_found = True
                    with z.open(info) as file:
                        # count lines from bytes stream, decode to text line by line
                        lines = sum(1 for line in io.TextIOWrapper(file, encoding='utf-8', errors='ignore'))
                    writer.writerow([package_name, f"{os.path.basename(zip_path)}::{info.filename}", lines])
            if not py_files_found:
                writer.writerow([package_name, f"{os.path.basename(zip_path)} (No Python files found)", ''])
    except Exception as e:
        writer.writerow([package_name, f"{os.path.basename(zip_path)} (Error reading archive)", str(e)])

def process_tar(tar_path, package_name, writer):
    """Process .tar or compressed tar archive and write .py files info to CSV."""
    try:
        with tarfile.open(tar_path) as tar:
            py_files_found = False
            for member in tar.getmembers():
                if member.isfile() and member.name.endswith('.py'):
                    py_files_found = True
                    f = tar.extractfile(member)
                    if f:
                        lines = sum(1 for line in io.TextIOWrapper(f, encoding='utf-8', errors='ignore'))
                        writer.writerow([package_name, f"{os.path.basename(tar_path)}::{member.name}", lines])
            if not py_files_found:
                writer.writerow([package_name, f"{os.path.basename(tar_path)} (No Python files found)", ''])
    except Exception as e:
        writer.writerow([package_name, f"{os.path.basename(tar_path)} (Error reading archive)", str(e)])

def list_package_py_files_to_csv(root_dir, csv_path):
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Package', 'Relative File Path', 'Line Count'])

        for package_name in sorted(os.listdir(root_dir)):
            package_path = os.path.join(root_dir, package_name)
            if os.path.isdir(package_path):
                py_files_found = False
                for dirpath, _, filenames in os.walk(package_path):
                    for file in filenames:
                        file_path = os.path.join(dirpath, file)
                        if file.endswith('.py'):
                            py_files_found = True
                            rel_path = os.path.relpath(file_path, package_path)
                            line_count = count_lines(file_path)
                            writer.writerow([package_name, rel_path, line_count])
                        elif file.endswith('.zip'):
                            process_zip(file_path, package_name, writer)
                        elif file.endswith(('.tar', '.tar.gz', '.tgz', '.tar.bz2', '.tbz')):
                            process_tar(file_path, package_name, writer)

                if not py_files_found:
                    # Check if no py files in directories and no archives found either:
                    # (Note: archives can still have python files so no "No Python files" here if archives found)
                    writer.writerow([package_name, '(No Python files found)', ''])

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    folder = filedialog.askdirectory(title="Select Root Directory")
    if folder:
        # Save CSV in the same directory as this script
        current_dir = os.path.dirname(os.path.abspath(__file__))
        csv_file = os.path.join(current_dir, 'package_files_report.csv')

        list_package_py_files_to_csv(folder, csv_file)
        print(f"Report saved to {csv_file}")
    else:
        print("No directory selected.")
