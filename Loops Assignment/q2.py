''''''
'''
2. Print the following patterns using loop :
a.
        *
        **
        ***
        ****
b.
        *
        ***
        *****
        ***
        *
c.
        1010101
        10101
        101
        1
d.
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
'''

print("------------------------A--------------------------------------------------")
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
print("------------------------b--------------------------------------------------")
'''
for i in range(1,6):
    if i%2!=0:
        for j in range(1,i+1):
            print("*",end=" ")
        print()
for i in range(5-2,-1,-1):
    if i%2!=0:
        for j in range(i,1):
            print("*",end=" ")
        print()
'''
h = eval(input("Enter diamond's height: "))
for x in range(h):
    print(" " * (h - x), "*" * (2 * x + 1))
for x in range(h - 2, -1, -1):
    print(" " * (h - x), "*" * (2 * x + 1))
print("------------------------c--------------------------------------------------")
# to make four iterations
i = 4
# while loop to make iterations
while i > 0:
    # number of digits in each row is (2*i)-1
    # in i is 4
    # number of digits is 2*4-1 = 7
    # when 3 - 5
    j = (2 * i) - 1
    # empty string
    a = ""
    # loop to make string
    # we will add 0 and 1 to string
    while j > 0:
        if j % 2 == 0:
            a = a + "0"
        else:
            a = a + "1"
        j = j - 1
    # 4-i is the space before the digits
    print(" " * (4 - i), a)
    i = i - 1
print("------------------------d--------------------------------------------------")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
