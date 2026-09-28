import numpy as np

A = np.array([
    [4, 1],
    [2, 3]
])

print(f'Shape: {np.shape(A)}')
detA = np.linalg.det(A)
inverse = True
if detA != 0:
    invA = np.linalg.inv(A)
else:
    inverse = False
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f'Determinate: {detA}')
print(f'Inverse: {inverse}')
print(f'Inverse: {invA}')
print(f'Eigenvalues: {eigenvalues}')
print(f'Eigenvectors: {eigenvectors}')
x = int(input("X = "))
y = int(input("Y = "))
v = np.array ([x,y])
magnitude = np.linalg.norm(v)
transformedA = A @ v
transformedMagnitude = np.linalg.norm(transformedA)
print(f'Magnitude: {magnitude}')
print(f'Transformed: {transformedA}')
print(f'Transformed Magnitude: {transformedMagnitude}')
if magnitude == transformedMagnitude:
    print("The magnitude has remained the same.")
else:
    print("The magnitude has changed.")

for i in range(len(eigenvalues)):
    lam = eigenvectors[:,i] * eigenvalues[i]
    vector = A @ eigenvectors[:,i]
    print(f'Eigenvector {i}:')
    print(f'Eigenvalues: {eigenvalues[i]}')
    print(f'Av: {vector}')
    print(f'λv: {lam}')
    print(f'Is Av = λv: {np.allclose(lam, vector)}')
