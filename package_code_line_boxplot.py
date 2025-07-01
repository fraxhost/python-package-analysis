import pandas as pd
import matplotlib.pyplot as plt

# Load and clean data
df = pd.read_csv('package_line_totals.csv')
df['Total Lines of Code'] = pd.to_numeric(df['Total Lines of Code'], errors='coerce')
df = df.dropna(subset=['Total Lines of Code'])

# Plot standard box plot
plt.figure(figsize=(12, 4))
plt.boxplot(df['Total Lines of Code'], vert=False, showfliers=True)
plt.xlabel('Total Lines of Code')
plt.title('Box Plot of Total Lines of Code')
plt.tight_layout()
plt.show()
