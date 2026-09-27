import numpy as np
def vector_info(v):
    print(v)
    magnitude = np.linalg.norm(v)
    print(magnitude)
    print(v/magnitude)
    print(np.dot(v,v))
v = np.array([2, -3, 6])
vector_info(v)