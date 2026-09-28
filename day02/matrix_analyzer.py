import numpy as np

A = np.array([
    [2, 3],
    [1, 4]
])

print("Matrix:")
print(A)

print("Dimensions:", A.shape)
det = np.linalg.det(A)
print("Determinant:", det)
inverse = np.linalg.inv(A)
print(inverse)
print(A @ inverse)
eigenvalues, eigenvectors = np.linalg.eig(A)
print(eigenvalues)
print(eigenvectors)