''''''
'''
9. Write a program in python to display the sum of the series [ 1+x+x^2/2!+x^3/3!+....]. Go to
the editor
Test Data :
Input the value of x :3
Input number of terms : 5
Expected Output :
The sum is : 16.375000
'''
from math import *

num = int(input("Enter Value of x:- "))
terms = int(input("Enter number of terms :- "))
series1 = []
sum = 0
series1.append(1 + num)
for i in range(2, terms):
    fact = factorial(i)
    print("fact:- ", fact)
    num2 = (num ** i) / fact
    series1.append(num2)
    print(num2)
for i in series1:
    sum = sum + i

print("The sum is :- ", sum)
