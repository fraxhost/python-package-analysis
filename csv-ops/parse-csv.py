import tkinter as tk
from tkinter import filedialog
import pandas as pd

def select_csv_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

def show_column_values(csv_path, column):
    try:
        df = pd.read_csv(csv_path, usecols=[column])
    except FileNotFoundError:
        print(f"File not found: {csv_path}")
        return
    except ValueError:
        print(f"Column '{column}' not found. Available columns: {pd.read_csv(csv_path, nrows=0).columns.tolist()}")
        return

    values = df[column].dropna().tolist()
    print(f"Values in '{column}':")
    for i in range(len(values)):
        print(i, values[i])

if __name__ == "__main__":
    path = select_csv_file()
    if path:
        col = 'Package Name'
        show_column_values(path, col)
    else:
        print("No file selected.")
