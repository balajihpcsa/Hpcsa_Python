'''
'''
'''
6. Find all occurrences of “USA” from right to left in a given string ignoring the case. also
display the position
Given:

str1 = "Welcome to USA. usa awesome, isn't it?
'''
str1 = "Welcome to USA. usa awesome, isn't it?"
str2=str1.lower()
substr="usa"
count=str2.count(substr)
print("Count of Occurrences of Substring:- ",count)

res = [i for i in range(len(str2)) if str2.startswith(substr, i)]
print("Position of Occurrences of Substring:- ",res)