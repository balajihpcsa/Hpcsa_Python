def addition(a, b=34, *t):
    print(a)
    print(b)
    s = a + b
    for num in t:
        s = s + num
    return s


print(addition(12, 13))
print(addition(12))
print(addition(12, 13, 23, 24, 25, 10, 22, 4))
