''''''

'''Write programs using lists in python
1. Reverse a given list in Python
aLsit = [100, 200, 300, 400, 500]
output:
[500, 400, 300, 200, 100]'''

sit = [100, 200, 300, 400, 500]
sit.reverse()
print(sit)

'''
2. Concatenate two lists index-wise
Given:
list1 = ["M", "na", "i", "Raj"]
list2 = ["y", "me", "s", "esh"]
output:
['My', 'name', 'is', 'Rajesh']'''
list1 = ["M", "na", "i", "Raj"]
list2 = ["y", "me", "s", "esh"]
list3 = []
for i in range(len(list1)):
    # list3[i] = list1.index(i) + list2.index(i)
    list3.insert(i, list1[i] + list2[i])
print(list3)

'''3. Given a Python list of numbers. Turn every item of a list into its square
aList = [1, 2, 3, 4, 5, 6, 7]
output:
[1, 4, 9, 16, 25, 36, 49]'''

aList = [1, 2, 3, 4, 5, 6, 7]
lst = []
for i in range(len(aList)):
    lst.insert(i, aList[i] ** 2)
print(lst)

'''4. Concatenate two lists in the following order
list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
output:
['Hello Students ', 'Hello Sir', 'welcome Students ', 'Welcome Sir']'''

list1 = ["Hello ", "Welcome "]
list2 = ["Students", "Sir"]
list3 = []
for i in range(len(list1)):
    for j in range(len(list2)):
        list3.insert(i, list1[i] + list2[j])
print(list3)

'''5. Given a two Python list. Iterate both lists simultaneously such that list1 should display item
in original order and list2 in reverse order
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
output:
10 400
20 300
30 200
40 100'''

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
lst = list2.reverse()
for i in range(len(list2)):
    print(list1[i], "  ", list2[i])

'''6.Remove empty strings from the list of strings

list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
output:
["Ashish", "Atharva", "Amit", "Revati"]'''
list1 = ["Ashish", "", "Atharva", "Amit", "", "Revati"]
tmp = ""
for tmp1 in list1:
    if tmp1 == tmp:
        list1.remove(tmp1)
print(list1)

'''7.Add item 7000 after 6000 in the following Python List
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
output:
[10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] '''
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].insert(2,7000)
print(list1)

'''8. Given a nested list extend it by adding the sub list ["h", "i", "j"] in such a way that it will look
like the following list
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
Sub List to be added = ["h", "i", "j"]
output:
['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']'''

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
subList = ["h", "i", "j"]

list1[2][1][2].extend(subList)
print(list1)

'''9. Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only
update the first occurrence of a value
list1 = [5, 10, 15, 20, 25, 50, 20]
output:
list1 = [5, 10, 15, 200, 25, 50, 20]
'''
list1 = [5, 10, 15, 20, 25, 50, 20]
if 20 in list1:
    pos =list1.index(20)
    list1[pos]=200
print(list1)

'''10. Given a Python list, remove all occurrence of 20 from the list
list1 = [5, 20, 15, 20, 25, 50, 20]
output:
[5, 15, 25, 50]'''
list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i==20:
        list1.remove(i)
print(list1)