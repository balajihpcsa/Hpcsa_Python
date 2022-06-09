fh = open("myfile.txt", 'r')

for ln in fh:
    ln=ln.rstrip("\n")
    print(ln)
fh.close()
