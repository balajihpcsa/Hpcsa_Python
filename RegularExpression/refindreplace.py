import re

s = "Something is there Somewhere"

s1 = re.sub("s.*?e", "any", s, count=2, flags=re.I)

print(s1)
