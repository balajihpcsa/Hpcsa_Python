courses = {"DBDA": 120, "DAC": 240}
print(courses["DBDA"])
courses["DBDA"] = 150
courses["DHPCSA"] = 10
print(courses["DBDA"])

for k in courses.keys():
    if courses[k] < 100:
        print(f"{k} ----- {courses[k]}")
for k, v in courses.items():
    if v < 100:
        print(f"{k} ----- {v}")

d = {"python": 60, "linux": 90, "perl": 20}
k = input("enter name :- ")
v = d.get(k, -2)
print(v)
v = d.setdefault("hpc", 65)
print(v)
print(d)

d1 = {"a": 10, "b": 20}
d2 = {"a": 200, "c": 45, "d": 300}
d1.update(d2)
print(d1)

d = {"a": 10, "b": 20, "c": 30, "x": 50}
v = d.pop("b")
print(v)
print(d)
x = d.popitem()
print(x)
print(d)

del (d["a"])
d.clear()
print(d)

d1 = {"a": 10, "b": 20, "c": 30, "x": 50}

