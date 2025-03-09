import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
cleaned_dataset_path = "international_energy_statistics_cleaned.csv"
df = pd.read_csv(cleaned_dataset_path)

# Pairplot to visualize relationships
plt.figure(figsize=(10, 10))
sns.pairplot(df, vars=['Energy Production', 'Energy Consumption', 'Renewable Energy', 'Non-Renewable Energy'])
plt.show()

# Boxplot to visualize the distribution of energy consumption by region
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Region', y='Energy Consumption')
plt.title('Energy Consumption by Region')
plt.xlabel('Region')
plt.ylabel('Energy Consumption')
plt.show()
