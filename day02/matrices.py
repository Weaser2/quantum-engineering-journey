import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print(A.shape)
I = np.eye(3)
print(I)
print(np.dot(A,I))

A_inv=np.linalg.inv(A)
python(A @ A_inv)