lst = [12, 13, 14, 15]
lst = [10, 20, "jssjdkjsk", "sagdjhbx", [12, 13, 15]]
print(lst[2])
print(lst[4][2])

lst = [100, 200, 300]
lst.append(400)
lst1 = ["a", "b", "c"]
lst.extend(lst1)

print(lst)
lst.insert(1, 101)
print(lst)

lst.pop()
print(lst)
lst.pop(1)
print(lst)

lst.reverse()
print(lst)
lst.reverse()
print(lst)
lst1.sort(reverse=True)
print(lst1)