a = 10
b = a
c = 10
print(id(a), id(b), id(c))
a = 20
d = 5
e = b - 5
print(id(a), id(b), id(c), id(d), id(e))
print(a is b)
print(d is e)
