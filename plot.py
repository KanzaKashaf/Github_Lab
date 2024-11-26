import pandas as pd
import matplotlib.pyplot as plt

# Define the dataset
data = pd.read_csv("wine-clustering.csv")

# Scatter plot for 'Alcohol' vs 'Proline'
plt.scatter(data['Alcohol'], data['Proline'])
plt.xlabel("Alcohol")
plt.ylabel("Proline")
plt.show()
