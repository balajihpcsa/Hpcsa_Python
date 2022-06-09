import numpy as np

a = np.array([10, 20, 30])
print(a.shape)
print(a.dtype)
print(type(a))
b = np.array([1, 2, 3])
print(a + b)
print(a - b)

a = np.array([[10.5, 20], [11, 22]])
b = np.arange(1, 8, 2).reshape(2, 2)
print(b)
print(np.dot(a, b))
print(a.dot(b))

print("**" * 70)

d = np.array([5, 6, 7, 8, 10, 11, 17, 18])
print(d[d >= 10])
