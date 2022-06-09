''''''
'''
1. Accept 10 integers from user and print their average value on the screen
'''

sum = 0
i = 0
while i < 10:
    num = int(input("Enter Number to add :- "))
    sum = sum + num
    i = i + 1
print("Average of 10 values is :- ", sum / 10)
