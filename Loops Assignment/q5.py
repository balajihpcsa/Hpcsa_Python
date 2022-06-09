''''''
'''
5. Given a number count the total number of digits in a number and also find sum of digits of
the number.
'''

num=input("Enter Number:- ")

d=0
sum=0
for i in num:
    d=d+1
    sum=sum+int(i)

print(f"Total number of digits in a {num} are {d}  and sum of digits of the number is {sum}")