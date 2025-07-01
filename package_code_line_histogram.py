import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('package_line_totals.csv')

# Convert LOC to numeric
df['Total Lines of Code'] = pd.to_numeric(df['Total Lines of Code'], errors='coerce')
df = df.dropna(subset=['Total Lines of Code'])

# Create bins: 0-1000, 1001-2000, 2001-3000, ..., up to the max value
max_loc = df['Total Lines of Code'].max()
bin_width = 1000
bins = list(range(0, int(max_loc) + bin_width, bin_width))
labels = [f"{b+1}-{b+bin_width}" if b > 0 else f"{b}-{b+bin_width}" for b in bins[:-1]]

# Categorize each package into a bin
df['LOC Range'] = pd.cut(df['Total Lines of Code'], bins=bins, labels=labels, right=True, include_lowest=True)

# Count packages per bin
range_counts = df['LOC Range'].value_counts().sort_index()

# Plot histogram of package counts per LOC range
plt.figure(figsize=(14, 6))
plt.bar(range_counts.index.astype(str), range_counts.values, color='skyblue', edgecolor='black')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Lines of Code Range')
plt.ylabel('Number of Packages')
plt.title('Packages per Lines of Code Range')
plt.tight_layout()
plt.show()
