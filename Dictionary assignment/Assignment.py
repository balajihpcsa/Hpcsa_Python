''''''

'''1. the two lists convert it into the dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30}
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
lst = {}
for k, v in zip(keys, values):
    lst[k] = v
print(lst)

'''
2. Merge following two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

Expected output:

{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
Solution:
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# ** operator unpack the dictionary and then merge bot dictionaries
dict3 = {**dict1, **dict2}
print(dict3)'''
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

'''3. Display the value of key history from the following dictionary
the value of key ‘history’ from the below dict
sampleDict = {
    "class":{
        "student":{
            "name":"Mike",
            "marks":{
                "physics":70,
                "history":80
            }
        }
    }
}
'''
sampleDict = {"class": {"student": {"name": "Mike", "marks": {"physics": 70, "history": 80}}}}
print(sampleDict.get("class").get("student").get("marks").get("history"))
'''
4. Delete set of keys from a dictionary

Given:

sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"

}
keysToRemove = ["name", "salary"]
'''
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
sampleDict.pop("name")
sampleDict.pop("salary")
print(sampleDict)
'''
5. display all the keys with value 200 from the following dictionary.
sampleDict = {'a': 100, 'b': 200, 'c': 300,’d’:200}'''
sampleDict = {'a': 100, 'b': 200, 'c': 300, 'd': 200}

for k in sampleDict.keys():
    if sampleDict[k] == 200:
        print(k)

'''6. Rename key city to location in the following dictionary

sampleDict = {
"name": "Kelly",
"age":25,
"salary": 8000,
"city": "New york"
}
Expected output:

{
"name": "Kelly",
"age":25,
"salary": 8000,
"location": "New york"
}'''
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sampleDict["location"] = sampleDict.pop("city")

print(sampleDict)

'''
7. display the key of a maximum value from the following dictionary

sampleDict = {
'Physics': 82,
'Math': 65,
'history': 75

}
'''
sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75

}
print(max(sampleDict.values()))
for k in sampleDict.keys():
    if sampleDict[k] == max(sampleDict.values()):
        print(k)
'''
8. Accept name and new salary for a employee, modify salary of the employee. display
appropriate message if salary modified. or if name not found.
note : the new salary should be > current salary otherwise show message wrong salary.
sampleDict = {
'emp1': {'name': 'Jhon', 'salary': 7500},
'emp2': {'name': 'Emma', 'salary': 8000},
'emp3': {'name': 'Brad', 'salary': 6500}
}
'''
sampleDict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

name = input("Enter name of emp :- ")
salary = int(input("Enter new salary:- "))

for emp in sampleDict.keys():
    value = sampleDict[emp]
    if value.get("name") == name:
        if salary > value["salary"]:
            sampleDict[emp]['salary'] = salary
            print(f"Salary Updated for {name}")
        else:
            print("wrong salary")
print(sampleDict)
