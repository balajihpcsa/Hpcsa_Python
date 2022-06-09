import os

print(os.getcwd())
os.chdir("F:\\")

lst=os.listdir()
for i in lst:
    if i == "test1.txt" or i=="test2.txt":
        print(i)
        ans = input("Delete (y/n):- ")
        if ans=="y":
            os.remove("./"+i)
print()
