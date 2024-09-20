import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./data.csv')

sentiment_by_company = data[['ticker', 'ticker_sentiment_score']].groupby('ticker').mean()

sentiment_by_company_sorted = sentiment_by_company.sort_values(by='ticker_sentiment_score', ascending=False)

top_10_gainers = sentiment_by_company_sorted.head(10)
top_10_losers = sentiment_by_company_sorted.tail(10)

top_10_combined = pd.concat([top_10_gainers, top_10_losers])

fig, ax = plt.subplots(figsize=(14, 8))

bars = ax.barh(top_10_combined.index, top_10_combined['ticker_sentiment_score'], 
               color=['lightgreen' if val >= 0 else 'salmon' for val in top_10_combined['ticker_sentiment_score']], 
               edgecolor='black')

ax.set_title('Top 10 Gaining and Losing Stocks by Sentiment Score', fontsize=20, fontweight='bold')
ax.set_xlabel('Average Sentiment Score', fontsize=14)
ax.set_ylabel('Stock Ticker', fontsize=14)

ax.grid(True, which='both', linestyle='--', linewidth=0.7, alpha=0.7)

for bar in bars:
    ax.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, 
            f'{bar.get_width():.2f}', 
            va='center', ha='left', fontsize=12, fontweight='bold')

plt.tight_layout()
plt.show()
