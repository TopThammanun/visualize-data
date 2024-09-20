import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data2.csv')

data['change_percentage'] = data['change_percentage'].str.rstrip('%').astype(float)

grouped_data = data.groupby('ticker').mean(numeric_only=True)

top_10_gainers_grouped = grouped_data.nlargest(10, 'change_percentage')
top_10_losers_grouped = grouped_data.nsmallest(10, 'change_percentage')

top_20_combined = pd.concat([top_10_gainers_grouped, top_10_losers_grouped])

fig, ax = plt.subplots(figsize=(14, 8))

bars = ax.barh(top_20_combined.index, top_20_combined['change_percentage'],
               color=['lightgreen' if val >= 0 else 'salmon' for val in top_20_combined['change_percentage']],
               edgecolor='black')

ax.set_title('Top 10 Gainers and Losers by Average Percentage Change (Grouped by Ticker)', fontsize=20, fontweight='bold')
ax.set_xlabel('Average Percentage Change', fontsize=14)
ax.set_ylabel('Stock Ticker', fontsize=14)

ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

for bar in bars:
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2,
            f'{bar.get_width():.2f}%', 
            va='center', ha='left', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
