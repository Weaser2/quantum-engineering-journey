import numpy as np

A = np.array([
    [0, -1],
    [1,  0]
])

v = np.array([1, 0])

result = A @ v

print("Original:", v)
print("Transformed:", result)