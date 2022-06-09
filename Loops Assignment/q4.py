''''''
'''
4. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every
integer input ). Print average and product of all numbers.
'''
ch = "y"
lst = []
while ch != 'q':
    num = int(input("Enter Number:- "))
    lst.append(num)
    ch = input("For quit press q or y for continue:- ")

print(lst)
sum = 0
product = 1
for i in lst:
    sum = sum + i
    product = product * i
print(f"Average of all numbers are {sum/len(lst)} and product of numbers is {product}")
