''''''
'''
2. Given two strings, s1 and s2, create a new string by appending s2 in the middle of s1

Given:
s1 = "Ault"
s2 = "Kelly"
Expected Output:
AuKellylt
'''

s1 = "Ault"
s2 = "Kelly"


def insertinbetweenstring(str1, str2):
    str3 = str1[:len(str1) // 2]
    str3 = str3 + str2
    str3 = str3+str1[len(str1) // 2:]
    return str3


print(insertinbetweenstring(s1, s2))
