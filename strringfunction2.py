s = "This is a cat where is your cat"
count = s.count("cat")
print(f"Number of occurrences :{count}")

print(s.find("cat"))

print(s.index("cat"))
pos = s.rfind("cat")
while pos != -1:
    print(pos)
    pos = s.rfind("cat", 0, pos - 1)

print(s.strip("cat"))
print(s.lstrip("cat"))
print(s.rstrip("cat"))

emp = "User1,manager,1234,Hr"
lst = emp.split(",")
print("|".join(lst))

s = "sdnhvjck12334568"
for i in s:
    if i.isalpha():
        print(i, end=" ")

print("\n----------------------\n")
s = "sdnhvjck@12334568,esdddf"
for i in s:
    if i.isalnum():
        print(i, end=" ")

for ch in s:
    if not ch.isdigit():
        print(ch)

