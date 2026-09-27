import numpy as np
A = np.array([
    [5, 6],
    [7, 8]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print(f'A: ')
print(A)

print(f'B: ')
print(B)

print("A + B: ")
print(A + B)

print("Element muiltiplication: ")
print(A * B)

print("Matrix multiplication: ")
print(A @ B)

print("Transpose of A: ")
print(A.T)