''''''
'''
Ask user number of terms to be generated of a series.
generate numbers for the following series and find its addition
[9 + 99 + 999 + 9999+........]
'''

num = int(input("Enter number to generate series of :-  "))
t = int(input("Enter terms to make series of :-  "))
sum = 0
nnum = num
for i in range(1, t + 1):
    sum = sum + nnum
    print(nnum, end=" ")
    nnum = nnum * 10 + num
print()
print(f"Sum is {sum}")
