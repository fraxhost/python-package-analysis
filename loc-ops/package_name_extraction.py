import pandas as pd
import csv

# Read CSV (with default header inference)
df = pd.read_csv('../csv/package_annotations_ryan.csv')

# Extract the "Package Name" column as a list
package_names = df['Package Name'].dropna().tolist()

# Load the LOC CSV
loc_df = pd.read_csv('../csv/package_loc.csv')  # your file with lines of code

# Create a mapping from Package to LOC
loc_map = dict(zip(loc_df['Package'], loc_df['Total Lines of Code']))

# Retrieve LOC for each package_name
results = {pkg: loc_map.get(pkg) for pkg in package_names}

# Define the CSV file path
csv_file_path = '../csv/package_loc_ryan.csv'

# Open the CSV file in write mode
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header row
    writer.writerow(['Package Name', 'Total Lines of Code'])
    
    # Write the data rows
    for package, loc in results.items():
        writer.writerow([package, loc])

print(f"Data successfully written to {csv_file_path}")