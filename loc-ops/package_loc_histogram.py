import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and clean data
df = pd.read_csv('../csv/package_loc_annotated.csv')
df['Total Lines of Code'] = pd.to_numeric(df['Total Lines of Code'], errors='coerce')
df = df.dropna(subset=['Total Lines of Code'])

# (Optional) Filter the desired range
df = df[df['Total Lines of Code'].between(5, 75)]

# 2. Define bin edges so that each integer has its own bin
min_loc = int(df['Total Lines of Code'].min())
max_loc = int(df['Total Lines of Code'].max())
bin_edges = np.arange(min_loc - 0.5, max_loc + 1.5, 1)
# This sets up bins: [4.5–5.5), [5.5–6.5), …, capturing exact integer values centrally :contentReference[oaicite:0]{index=0}

# 3. Plot histogram
counts, edges, patches = plt.hist(
    df['Total Lines of Code'],
    bins=bin_edges,
    edgecolor='black',
    align='mid'
)

plt.xlabel('Lines of Code')
plt.ylabel('Package Count')
plt.title('Histogram with Exact Integer Bins')
plt.xticks(range(min_loc, max_loc + 1))
plt.tight_layout()
plt.show()

# 4. Export bin counts to CSV
hist_df = pd.DataFrame({
    'bin_value': range(min_loc, max_loc + 1),
    'count': counts.astype(int)
})
hist_df.to_csv('../csv/package_loc_annotated_bins_counts.csv', index=False)
print("Saved integer bin counts to loc_integer_bins_counts.csv")
