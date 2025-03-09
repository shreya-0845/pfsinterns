import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
cleaned_dataset_path = "airline_delay_and_cancellation_data_cleaned.csv"
df = pd.read_csv(cleaned_dataset_path)

# Pairplot to visualize relationships
plt.figure(figsize=(10, 10))
sns.pairplot(df, vars=['ArrDelay', 'DepDelay', 'AirTime', 'Distance', 'CarrierDelay', 'WeatherDelay', 'NASDelay', 'SecurityDelay', 'LateAircraftDelay'])
plt.show()

# Boxplot to visualize the distribution of delays by airline
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='UniqueCarrier', y='ArrDelay')
plt.title('Arrival Delays by Airline')
plt.xlabel('Airline')
plt.ylabel('Arrival Delay (minutes)')
plt.show()
