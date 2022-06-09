''''''
'''
7. Accept 20 numbers from user and display sum of only even numbers.
'''
n=1
sum = 0
while n!=11:
    num=int(input("Enter number"))
    if n%2==0:
        sum=sum+num
    n=n+1
print(sum)
