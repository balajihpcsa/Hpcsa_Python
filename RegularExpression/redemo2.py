import re

s = "Something is there Somewhere"

lst = re.findall("S.*?e", s, re.I)
if lst is not None:
    print(lst)
    for i in lst:
        print(i)
else:
    print("Not Found")

print("-" * 100)

lst = re.finditer("S.*?e", s, re.I)
if lst is not None:
    print(lst)
    for i in lst:
        print(i.span())
        print(i.group())
else:
    print("Not Found")
