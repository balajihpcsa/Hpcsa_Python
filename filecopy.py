import os

fh = open(r"myfile.txt")
if os.path.exists("myfilecopy.txt"):
    print("File exist")
    fh1 = open("myfilecopy.txt", "a")
else:
    print("Does not exist")
    fh1 = open("myfilecopy.txt", "w")
for ln in fh:
    fh1.write(ln)
fh.close()
fh1.close()
