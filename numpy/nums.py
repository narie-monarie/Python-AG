import numpy as np
a = np.array([0, 1, 2, 3, 4])
print(a.ndim)  # Dimensions of the Array
# a.shape(value)  # Dimensions size of the Array

# Vector addition

u = [1, 0]
v = [0, 1]
z = []

for n, m in zip(u, v):
    z.append(n+m)

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
a = np.dot(u, v)
# multiply Vectors
print(2*z)
print(a)
