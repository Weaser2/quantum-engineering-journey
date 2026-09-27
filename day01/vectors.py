import numpy as np 
v = np.array([3, 4])
print(v)
print(type(v))
print(v.shape)

a = np.array([1, 2])
b = np.array([3, 4])

print(f'Addition: {a + b}')
print(f'Subtraction: {a - b}')
print(f'Multiplication: {a * b}')
print(f'Division: {a / b}')
print(f'Dot product: {np.dot(a, b)}')

magnitude1 = np.linalg.norm(a)
magnitude2 = np.linalg.norm(b)

print(f'Magnitude1: {magnitude1}, Magnitude2: {magnitude2}')

normalized1 = a / magnitude1
normalized2 = b / magnitude2

print(f'Normalized1: {normalized1}, Normalized2: {normalized2}')
print(f'New magnitude1: {np.linalg.norm(normalized1)}, New magnitude2: {np.linalg.norm(normalized2)}')