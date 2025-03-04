import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 🚀 AI/ML Learning Journey - Step 3 - Math & Stats for ML

# ✅ Sample Data (Heights in cm)
data = [160, 165, 170, 175, 180, 185, 190, 195, 200, 205]

# ✅ Mean (Average)
mean = np.mean(data)
print(f"Mean (Average): {mean} cm")

# ✅ Median (Middle Value)
median = np.median(data)
print(f"Median: {median} cm")

# ✅ Mode (Most Frequent - for categorical data like survey results)
# Using pandas for mode (since NumPy doesn’t have mode in basic version)
df = pd.DataFrame(data, columns=['Height'])
mode = df['Height'].mode()[0]
print(f"Mode: {mode} cm")

# ✅ Variance (Spread of Data)
variance = np.var(data)
print(f"Variance: {variance:.2f}")

# ✅ Standard Deviation (How much data varies from mean)
std_dev = np.std(data)
print(f"Standard Deviation: {std_dev:.2f}")

# ✅ Correlation Matrix (Imagine you had multiple features like height, weight, age)
df['Weight'] = [60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
print("\nCorrelation Matrix:")
print(df.corr())

# ✅ Probability Example (Dice Roll)
prob = 1/6
print(f"\nProbability of rolling a 6 on a fair die: {prob:.2f}")

# ✅ Plot Normal Distribution (Simulated Data)
normal_data = np.random.normal(mean, std_dev, 1000)
plt.hist(normal_data, bins=30, density=True, alpha=0.6, color='g')

# Overlay actual normal curve
from scipy.stats import norm
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mean, std_dev)
plt.plot(x, p, 'k', linewidth=2)
plt.title("Normal Distribution Curve")
plt.show()

print("✅ Step 3 - Math & Stats Completed!")
