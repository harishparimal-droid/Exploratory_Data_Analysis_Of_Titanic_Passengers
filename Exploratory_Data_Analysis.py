import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset
df = pd.read_csv('Final-Titanic-Dataset.csv')

# 1. Generate summary statistics
summary_stats = df.describe()
print(summary_stats)

# 2. Histogram of Age_Years
plt.figure(figsize=(12,5))
sns.histplot(df['Age_Years'].dropna(), kde=True, bins=30)
plt.title('Histogram of Age_Years')
plt.show()

# 3. Boxplot for Fare_Price
plt.figure(figsize=(6,4))
sns.boxplot(y=df['Fare_Price'])
plt.title('Boxplot of Fare_Price')
plt.show()

# 4. Convert Passenger_Class from string to numeric
class_map = {'1st': 1, '2nd': 2, '3rd': 3}
df['Passenger_Class'] = df['Passenger_Class'].map(class_map)

# 5. Pairplot for numeric features
numeric_cols = ['Age_Years', 'Sibling_Spouse_Count', 'Parent_Child_Count', 'Fare_Price', 'Passenger_Class']
sns.pairplot(df[numeric_cols].dropna())
plt.show()

# 6. Correlation matrix heatmap
correlation_matrix = df[numeric_cols].corr()
plt.figure(figsize=(10,7))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()
