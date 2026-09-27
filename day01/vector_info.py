import numpy as np
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
vector1 = np.array([num1, num2])
print(f'Vector: {vector1}')
print(f'Magnitude: {np.linalg.norm(vector1)}')
print(f'Normalized vector: {vector1/(np.linalg.norm(vector1))}')
print(f'Dot product: {np.dot(vector1, vector1)}')
