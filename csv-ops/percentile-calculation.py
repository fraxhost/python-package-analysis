import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os

# Save output in current directory
OUTPUT_FILENAME = "output_with_percentile.csv"
OUTPUT_PATH = os.path.join(os.getcwd(), OUTPUT_FILENAME)

def select_csv_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Select input CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    root.destroy()
    return file_path

def add_percentile_and_save(input_path, output_path):
    df = pd.read_csv(input_path)
    if 'Total Lines of Code' not in df.columns:
        print("Error: 'Total Lines of Code' column not found.")
        print("Available columns:", df.columns.tolist())
        return

    df['Percentile'] = df['Total Lines of Code'].rank(pct=True) * 100
    df.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    input_path = select_csv_file()
    if input_path:
        add_percentile_and_save(input_path, OUTPUT_PATH)
    else:
        print("No file selected.")
