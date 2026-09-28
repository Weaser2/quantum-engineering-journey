import numpy as np

z = 2 + 5j

print("Complex number:", z)
print("Real:", z.real)
print("Imaginary:", z.imag)
print("Magnitude:", abs(z))
print("Conjugate:", np.conj(z))

z1 = 2 + 3j
z2 = 4 + 1j

print(z1 * z2)