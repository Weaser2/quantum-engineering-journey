import numpy as np

A = np.array([
    [4, 1],
    [2, 3]
])

print("Shape:", np.shape(A))

det = np.linalg.det(A)
print("Determinant:", det)

if det != 0:
    print("Inverse:")
    print(np.linalg.inv(A))
else:
    print("NO INVERSE!")

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)