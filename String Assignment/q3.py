''''''
'''
3. two strings, s1, and s2 return a new string made of the first, middle, and last characters each
input string
Given:

s1 = "America"
s2 = "Japan"
Expected Output:
AJrpan
'''


def mix_string(s1, s2):
    first_char = s1[:1] + s2[:1]
    middle_char = s1[int(len(s1) / 2):int(len(s1) / 2) + 1] + s2[int(len(s2) / 2):int(len(s2)/ 2) + 1]
    last_char = s1[len(s1) - 1] + s2[len(s2) - 1]
    res = first_char + middle_char + last_char
    print("Mix String is ", res)

s1 = "America"
s2 = "Japan"
mix_string(s1, s2)
