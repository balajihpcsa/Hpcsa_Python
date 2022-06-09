def addition(a, b):
    a = a + 10
    b = b + 20
    return a + b


def addition1(a, b):
    a = a + 10
    b = b + 20
    return a, b, a + b


s = addition(12, 13)
print(s)
d = addition1(10, 20)
print(d)
