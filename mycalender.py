num = int(input("Enter Number :- "))
startday = int(input("Enter number between (0-6) :- "))

print("mon\ttue\twed\tthu\tfri\tsat\tsun")

cnt = startday

print("\t" * startday,end=" ")
for i in range(1,num+1):
    print(i,end="\t")
    cnt=cnt+1
    if(cnt==7):
       print()
       cnt=0