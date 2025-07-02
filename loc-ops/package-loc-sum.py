import csv
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict

def sum_package_line_counts(csv_path, output_path):
    package_sums = defaultdict(int)

    # Read the existing CSV
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            package = row['Package']
            line_count = row['Line Count'].strip()

            if line_count.isdigit():
                package_sums[package] += int(line_count)

    # Write the summary CSV
    with open(output_path, mode='w', newline='', encoding='utf-8') as out:
        writer = csv.writer(out)
        writer.writerow(['Package', 'Total Lines of Code'])
        for package, total_lines in sorted(package_sums.items()):
            writer.writerow([package, total_lines])

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Set default folder to the script’s directory
    default_dir = os.path.dirname(os.path.abspath(__file__))

    # Open file picker starting in the script directory
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
    csv_file = filedialog.askopenfilename(title="Select CSV File", initialdir=default_dir, filetypes=filetypes)

    if not csv_file:
        print("No CSV file selected.")
    else:
        output_dir = os.path.dirname(os.path.abspath(csv_file))
        output_csv = os.path.join(output_dir, 'package_line_totals.csv')

        sum_package_line_counts(csv_file, output_csv)
        messagebox.showinfo("Success", f"Summary saved to:\n{output_csv}")
