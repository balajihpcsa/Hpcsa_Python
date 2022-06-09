''''''
'''
1. Reverse the following tuple

aTuple = (10, 20, 30, 40, 50,60)
Expected output:
(60,50, 40, 30, 20, 10)
'''
aTuple = (10, 20, 30, 40, 50, 60)
r = aTuple[::-1]
print(r)

'''
2. display value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
'''
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aTuple[1][1])

'''
3. Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40)
'''
aTuple = (10, 20, 30, 40)
a,b,c,d= aTuple
print(a,b,c,d)

'''
4. Swap the following two tuples
tuple1 = (11, 22)
tuple2 = (99, 88)
Expected output:
tuple1 = (99, 88)
tuple2 = (11, 22)
'''
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1,tuple2=tuple2,tuple1
print("tuple 1 : ",tuple1)
print("tuple 2 : ",tuple2)
'''
5. Copy element 44 and 55 from the following tuple into a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)
Expected output:
tuple2: (44, 55)
'''
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=tuple1[3:5]
print(tuple2)


'''
6. Modify the first item (22) of a list inside a following tuple to 200

tuple1 = (11, [22, 33], 44, 55)
Expected output:
tuple1: (11, [200, 33], 44, 55)
'''
tuple1 = (11, [22, 33], 44, 55)

tuple1[1][0]=200
print(tuple1)