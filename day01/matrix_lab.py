import numpy as np
A = np.array([
    [0,-1],
    [1, 0]
])
x = int(input("Enter X: "))
y = int(input("Enter Y: "))
v = np.array([x, y])
result = A @ v
print(f'Original vector: {v}')
print(f'Transformed vecotr: {result}')
print(f'Original vector magnitude: {np.linalg.norm(v)}')
print(f'Transformed vector magnitude: {np.linalg.norm(result)}')