import numpy as np

A = np.array([
    [2, 1],
    [1, 2]
])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(eigenvalues)

print("Eigenvectors:")
print(eigenvectors)

v = eigenvectors[:, 0] # eigenvector
lam = eigenvalues[0] # lamda symbol and eigenvector

print("Eigenvalue:", lam)
print("Eigenvector:", v)

print("A @ v:", A @ v)
print("lambda * v:", lam * v)

for i in range(len(eigenvalues)):
    v = eigenvectors[:, i]
    lam = eigenvalues[i]

    print("Eigenvalue:", lam)
    print("Eigenvector:", v)
    print("A @ v:", A @ v)
    print("lambda * v:", lam * v)
    print()