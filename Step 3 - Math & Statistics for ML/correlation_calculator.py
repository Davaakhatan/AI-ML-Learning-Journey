import numpy as np

X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])

def calculate_correlation(x, y):
    mean_x, mean_y = np.mean(x), np.mean(y)
    num = np.sum((x - mean_x) * (y - mean_y))
    den = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
    return num / den

corr = calculate_correlation(X, Y)
print(f"Correlation: {corr:.2f}")
