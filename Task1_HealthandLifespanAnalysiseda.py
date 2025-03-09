import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
cleaned_dataset_path = "Life Expectancy Data Cleaned.csv"
df = pd.read_csv(cleaned_dataset_path)

# Pairplot to visualize relationships
plt.figure(figsize=(10, 10))
sns.pairplot(df, vars=['Life expectancy ', 'Adult Mortality', 'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B', 'Measles ', 'BMI ', 'under-five deaths ', 'Polio', 'Total expenditure', 'Diphtheria ', 'HIV/AIDS', 'GDP', 'Population', 'thinness  1-19 years', 'Income composition of resources', 'Schooling'])
plt.show()

# Boxplot to visualize the distribution of life expectancy by country status
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Status', y='Life expectancy ')
plt.title('Life Expectancy by Country Status')
plt.xlabel('Country Status')
plt.ylabel('Life Expectancy')
plt.show()
