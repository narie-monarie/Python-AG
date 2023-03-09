import numpy as np

a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
b = np.array(a)
print(b)
print(b.ndim, b.shape, b.size)
print(b[0, 0:2], b[0:2, 2])

c = np.array([[0, 1, 1], [1, 0, 1]])
d = np.array([[1, 1], [1, 1], [-1, 1]])
e = np.dot(c, d)
print(e)
