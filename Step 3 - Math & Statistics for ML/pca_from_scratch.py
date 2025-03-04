import numpy as np

# Sample 2D data
X = np.array([
    [2.5, 2.4],
    [0.5, 0.7],
    [2.2, 2.9],
    [1.9, 2.2],
    [3.1, 3.0],
])

# Step 1: Standardize data
mean = np.mean(X, axis=0)
X_centered = X - mean

# Step 2: Compute covariance matrix
cov_matrix = np.cov(X_centered.T)

# Step 3: Compute eigenvalues & eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

# Step 4: Project data onto first principal component
pc1 = eigenvectors[:, 0]
projected = X_centered @ pc1

print("First Principal Component:", pc1)
print("Projected Data (1D):", projected)
