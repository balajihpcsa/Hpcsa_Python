fnum = int(input("Enter First Number :- "))
snum = int(input("Enter Second Number :- "))
tnum = int(input("Enter Third Number :- "))

if fnum < snum and fnum < tnum:
    print(f"Minimum Number is :{fnum}")
elif snum < fnum and snum < tnum:
    print(f"Minimum Number is :{snum}")
else:
    print(f"Minimum Number is :{tnum}")
