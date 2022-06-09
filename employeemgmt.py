import os

lst = []
choice = 0


def readdata():
    fh = open("employeedata.dat", 'r')
    for ln in fh:
        ln = ln.rstrip("\n")
        lst.append(ln)
    fh.close()


if os.path.exists("employeedata.dat"):
    readdata()


def writedata():
    fh = open("employeedata.dat", "w")
    for emp in lst:
        fh.write(emp + "\n")
    fh.close()


def searchbyid(empid):
    for idx, ln in enumerate(lst):
        lst1 = ln.split(":")
        if lst1[0] == empid:
            return ln, idx
        else:
            return None,


def deletebyid(empid):
    emp, _ = searchbyid(empid)
    if emp != None:
        lst.remove(emp)
        return True
    else:
        return False


def addnewemployee():
    empno = input("Enter Number :- ")
    ename = input("Enter Name :- ")
    sal = input("Enter Salary :- ")
    dept = input("Enter Department :- ")
    s = f"{empno}:{ename}:{sal}:{dept}"
    lst.append(s)
    print(lst)


def displayall():
    for ln in lst:
        lst1 = ln.split(":")
        print(f"Empno : {lst1[0]}")
        print(f"Emp name : {lst1[1]}")
        print(f"Salary : {lst1[2]}")
        print(f"Department : {lst1[3]}")
        print("-" * 70)


def modifysalary(empid, sal):
    emp, pos = searchbyid(empid)
    if emp != None:
        lst1 = emp.split(":")
        lst1[2] = sal
        lst[pos] = ":".join(lst1)
        return True
    else:
        return False


def countbydept():
    d = {}
    for ln in lst:
        lst1 = ln.split(":")
        dept = lst1[3]
        v = d.get(dept, -1)
        if v != -1:
            d[dept] = d[dept] + 1
        else:
            d[dept] = 1
    return d


while choice != 7:

    print("""
    1. add new employee
    2. delete by id
    3. modify salary
    4. display all
    5. display by id
    6. count by dept
    7. exit
    """)

    choice = int(input("Enter choice:- "))

    match choice:
        case 1:
            addnewemployee()
        case 2:
            empid = input("Enter id for search :- ")
            status = deletebyid(empid)
            if status == True:
                print("Deleted Successfully")
            else:
                print("Not Found")
        case 3:
            empid = input("Enter id for search :- ")
            sal = input("Enter Salary :- ")
            status = modifysalary(empid, sal)
            if status == True:
                print("Modified Successfully")
            else:
                print("Not Found")
        case 4:
            displayall()
        case 5:
            empid = input("Enter id for search :- ")
            emp, _ = searchbyid(empid)
            if emp != None:
                lst1 = emp.split(":")
                print(f"Empno : {lst1[0]}")
                print(f"Emp name : {lst1[1]}")
                print(f"Salary : {lst1[2]}")
                print(f"Department : {lst1[3]}")
                print("-" * 70)
        case 6:
            d = countbydept()
            for k, v in d.items():
                print(f"{k} --- > {v}")
        case 7:
            writedata()
            print("Thank You for visiting Us")
