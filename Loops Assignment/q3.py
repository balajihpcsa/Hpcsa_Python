''''''
'''
3. Write a program to find greatest common divisor (GCD) or highest common factor (HCF) of
given two numbers.
'''


def gcd(num1, num2):
    if num1 > num2:
        small = num2
    else:
        small = num1
    for i in range(1, small + 1):
        if ((num1 % i == 0) and (num2 % i == 0)):
            gcd = i
    return gcd


num1 = int(input("Enter First Number :- "))
num2 = int(input("Enter Second Number :- "))

print(f"Gcd of {num1} and {num2} is :- ", gcd(num1, num2))
