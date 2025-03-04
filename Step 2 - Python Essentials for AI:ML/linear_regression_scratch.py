import numpy as np

# Sample data (X = years of experience, y = salary in $1000s)
X = np.array([1, 2, 3, 4, 5, 6])
y = np.array([30, 35, 45, 50, 60, 70])

def compute_slope_and_intercept(X, y):
    n = len(X)
    mean_x = np.mean(X)
    mean_y = np.mean(y)

    num = np.sum((X - mean_x) * (y - mean_y))
    den = np.sum((X - mean_x)**2)

    m = num / den
    b = mean_y - m * mean_x
    return m, b

m, b = compute_slope_and_intercept(X, y)
print(f"y = {m:.2f}x + {b:.2f}")

def predict(x):
    return m * x + b

predicted = [predict(xi) for xi in X]
print("Predicted salaries:", predicted)
