import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('D:/python-project/Global Renewable Energy/global_renewable_energy_trends_2000_2024.csv')

# Line plot
plt.figure(figsize=(10, 6))
for country in df['Country'].unique():
    country_data = df[df['Country'] == country]
    plt.plot(country_data['Year'], country_data['Renewable_Energy_Percentage'], label=country)

plt.title('Renewable Energy Adoption Trends (2000-2024)')
plt.xlabel('Year')
plt.ylabel('Renewable Energy Percentage (%)')
plt.legend(title='Country')
plt.grid(True)
plt.tight_layout()

plt_path_line = './Global Renewable Energy/renewable_energy_trends_line_chart.png'
plt.savefig(plt_path_line)
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
data_2024 = df[df['Year'] == 2024]
plt.bar(data_2024['Country'], data_2024['Renewable_Energy_Percentage'], color='skyblue')
plt.title('Renewable Energy Comparison (2024)')
plt.xlabel('Country')
plt.ylabel('Renewable Energy Percentage (%)')
plt.xticks(rotation=45)
plt.tight_layout()

plt_path_bar = './Global Renewable Energy/renewable_energy_comparison_bar_chart_2024.png'
plt.savefig(plt_path_bar)
plt.show()

# Heatmap
heatmap_data = df.pivot(index="Year", columns="Country", values="Renewable_Energy_Percentage")
plt.figure(figsize=(12, 8))
sns.heatmap(heatmap_data, cmap='YlGnBu', annot=False)

plt.title('Renewable Energy Growth Over Time by Country (2000-2024)')
plt.xlabel('Country')
plt.ylabel('Year')
plt.tight_layout()

plt_path_heatmap = './Global Renewable Energy/renewable_energy_trends_heatmap.png'
plt.savefig(plt_path_heatmap)
plt.show()

print(f"Visualizations saved to {plt_path_line}, {plt_path_bar}, and {plt_path_heatmap}")
