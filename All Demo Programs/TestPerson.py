import os
from personclass import Person

choice = 0
lst = []


def readdata():
    with open("persondata.dat") as fh:
        for ln in fh:
            ln = ln.rstrip("\n")
            lst1 = ln.split(":")
            p = Person(int(lst1[0]), lst1[1], lst1[2])
            lst.append(p)


def writedate():
    with open("persondata.dat", "w") as fh:
        for ob in lst:
            s = f"{ob.get_pid()}:{ob.get_pname()}:{ob.get_mob()}\n"
            fh.write(s)


if os.path.exists("persondata.dat"):
    readdata()


def addnewperson():
    pid = int(input("Enter id:- "))
    pname = input("Enter name:- ")
    mob = input("Enter Mobile ")
    p = Person(pid, pname, mob)
    lst.append(p)


def displayall():
    for ob in lst:
        print(ob)
        print("-" * 80)


def searchbyid(pid):
    for idx, ob in enumerate(lst):
        if ob.get_pid() == pid:
            return ob, idx
    return None, -1


def deleteperson(pid):
    ob, pos = searchbyid(pid)
    if ob != None:
        lst.remove(ob)
        return True
    else:
        return False


def modifyperson(pid, mob):
    ob, pos = searchbyid(pid)
    if ob != None:
        ob.set_mob(mob)
        return True
    else:
        return False


while choice != 7:
    print("""
    1. Add New Person
    2. search Person by pid
    3. modify data
    4. delete person
    5. display all
    6. display all whose name starts with given character
    7. exit
    """)

    choice = int(input("Enter Choice :- "))
    match choice:
        case 1:
            addnewperson()
        case 2:
            pid = int(input("enter pid:"))
            p, _ = searchbyid(pid)
            if p != None:
                print(p)
            else:
                print("none")
        case 3:
            pid = int(input("enter pid:"))
            mob = int(input("enter mob"))
            status = modifyperson(pid, mob)
            if status:
                print("modify successfully")
            else:
                print("not found")
        case 4:
            pid = int(input("enter pid:"))
            status = deleteperson(pid)
            if status:
                print("deleted successfully")
            else:
                print("not found")
        case 5:
            displayall()
        case 6:
            pass
        case 7:
            writedate()
            print("Thank you For visiting us !!!! ")
        case _:
            print("Wrong Choice ??")
