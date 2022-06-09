''''''
'''
4. Given an input string with the combination of the lower and upper case arrange characters
in such a way that all lowercase letters should come first.
'''

str1 = "PytHONStudy"
lower = []
upper = []
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted_string = ''.join(lower + upper)
print("arranging characters giving precedence to lowercase letters:")
print(sorted_string)
