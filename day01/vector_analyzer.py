import numpy as np
x = int(input("Enter X1: "))
y = int(input("Enter Y1: "))
z = int(input("Enter Z1: "))
vector1 = np.array([x,y,z])
print(f'Vector: {vector1}')
magnitude1 = np.linalg.norm(vector1)
print(f'Magnitude: {magnitude1}')
normalized1 = vector1/magnitude1
print(f'Normalized Vector: {normalized1}')
x2 = int(input("Enter X2: "))
y2 = int(input("Enter Y2: "))
z2 = int(input("Enter Z2: "))
vector2 = np.array([x2,y2,z2])
print(f'Vector: {vector2}')
magnitude2 = np.linalg.norm(vector2)
print(f'Magnitude: {magnitude2}')
normalized2 = vector2/magnitude2
print(f'Normalized Vector: {normalized2}')
print(f'Vector addition: {vector1+vector2}')
print(f'Vector subtraction: {vector1-vector2}')
print(f'Dot product: {np.dot(vector1,vector2)}')
if magnitude1 == magnitude2:
    print(f'Magnitude 1 and Magnitude 2 have the same magnitude of {magnitude1}.')
else:
    print(f'Magnitude 1 and Magnitude 2 do not have the same magnitude')