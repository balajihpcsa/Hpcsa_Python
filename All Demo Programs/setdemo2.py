s = {10, 20, 30, 40, 50}
t = {100, 200, 300, 40, 50}
print("Union", s | t)
print("Intersection", s & t)
print("difference", s - t)
print("Symmetric-Difference ", s ^ t)
a = s - t
print("difference-update ", a)
r = s ^ t
print("Symmetric-Difference-update ", r)
