''''''
'''
5. create a third-string made of the first char of s1 then the last char of s2, Next, the second
char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the
result.

Given:
s1 = "Abc"
s2 = "Xyz"
Expected Output:
AzbycX
'''
s1 = "Abcd"
s2 = "Xyz"

s3 = ''

if len(s1) > len(s2):
    minl = len(s2)
else:
    minl = len(s1)

for i in range(minl):
    s3 += s1[i]
    s3 += s2[-i - 1]
if len(s1) > minl:
    s3 += s1[minl:]
else:
    s3 += s2[minl:]
print(s3)
