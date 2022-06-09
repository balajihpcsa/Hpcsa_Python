import re

s = "This is home"
m = re.match("^\w+\s\w+\s\w+$", s)
if m != None:
    print(m.span())
    print(m.group())
else:
    print("Not found")

s = "Something is there"
m = re.search("t.*?e",s)
if m != None:
    print(m.span())
    print(m.group())
else:
    print("Not found")
