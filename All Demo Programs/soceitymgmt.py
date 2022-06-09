# soc = {}
soc = {"A": ["a", "b", "c"], "B": ["a", "g", "c"], "C": ["i", "b", "c"], "D": ["a", "e", "c"], "E": ["a", "b", "j"]}


def addnewowner():
    ans = "y"
    bldg = input("Enter bldg name")
    lst = []
    v = soc.get(bldg, -1)
    if v == -1:
        print("Building not exist")
    else:
        while ans != "n":
            nm = input("Enter owner name")
            lst.append(nm)
            ans = input("Continue y/n")
        tmp = soc[bldg]
        tmp.extend(lst)
        soc[bldg] = tmp
        print("Owner added")
        return soc


def addnewbldg():
    bldg = input("Enter bldg name")
    lst = []
    ans = "y"
    while ans == "y":
        nm = input("Enter owner name")
        lst.append(nm)
        ans = input("Continue y/n")
    v = soc.get(bldg, -1)
    if v == -1:
        soc[bldg] = lst
        return 1
    else:
        ans = input("Overwrite (y/n):- ")
        if ans == "y":
            soc[bldg] = lst
            return 2
        else:
            return 3


def displayall():
    for k, v in soc.items():
        print(f"{k}------------>{','.join(v)}")


def displaybyownername(nm):
    blist = []
    for k, v in soc.items():
        if nm in v:
            blist.append(k)
    if len(blist) == 0:
        return None
    else:
        return blist


choice = 0


def changeowner(onm, nnm):
    blist = displaybyownername(onm)
    if blist != None and len(blist) > 1:
        print(f"old Owner is Found in following buildings :- {','.join(blist)}")
        bldg = input("Select the bldg :- ")
        if bldg in blist:
            lst = soc[bldg]
            pos = lst.index(onm)
            lst[pos] = nnm
            return True
        else:
            print("Wrong Choice!")
            ch = input("do you want to try again (y/n)")
            if ch == "y":
                changeowner(onm, nnm)
                return True
            else:
                return 10

    elif blist != None and len(blist) == 1:
        bldg = blist[0]
        lst = soc[bldg]
        pos = lst.index(onm)
        lst[pos] = nnm
        return True
    else:
        return False


def deleteowner(onm):
    blist = displaybyownername(onm)
    if blist != None and len(blist) > 1:
        print(f"old Owner is Found in following buildings :- {','.join(blist)}")

        bldg = input("Select the bldg :- ")
        if bldg in blist:
            lst = soc[bldg]
            pos = lst.index(onm)
            lst.pop(pos)
            return True
        else:
            print("Wrong Choice!")
            ch = input("do you want to try again (y/n)")
            if ch == "y":
                deleteowner(onm)
            else:
                return 10
    elif blist != None and len(blist) == 1:
        bldg = blist[0]
        lst = soc[bldg]
        pos = lst.index(onm)
        lst.pop(pos)
        return True
    else:
        return False


def deletebldg(bldg):
    v = soc.keys()
    if bldg in v:
        soc.pop(bldg)
        return True
    else:
        return False


def changebldgname(obldg, nbldg):
    v = soc.keys()
    if obldg in v:
        lst = soc.pop(obldg)
        soc[nbldg] = lst
        return True
    else:
        return False


while (choice != 9):
    print(
        """
    1. add new member in bldg
    2. add new bldg
    3. delete a bldg
    4. delete the owner
    5. modify the owner
    6. change bldg name
    7. display all
    8. display by owner
    9. exit
    """
    )
    choice = int(input("Enter Choice:- "))
    match choice:
        case 1:
            status = addnewowner()
        case 2:
            status = addnewbldg()
            if status == 1:
                print("new bldg added")
            elif status == 2:
                print("bldg found and owner updated")
            elif status == 3:
                print("bldg found but not modified")
        case 3:
            bldg = input("Enter bldg name :- ")
            status = deletebldg(bldg)
            if status:
                print("Bldg deleted")
            else:
                print(f"no bldg found with {bldg}")

        case 4:
            onm = input("Enter owner name :- ")
            status = deleteowner(onm)
            if status == True:
                print("owner deleted")
            elif status == 10:
                print("Owner found but not deleted")
            else:
                print(f"no owner found with {onm}")
        case 5:
            onm = input("Enter old owner name :- ")
            nnm = input("Enter new owner name :- ")
            status = changeowner(onm, nnm)
            if status == True:
                print("owner name modified")
            elif status == 10:
                print("Owner found but not changed")
            else:
                print(f"no owner found with {onm}")
        case 6:
            obldg = input("Enter old bldg name :- ")
            nbldg = input("Enter New bldg name:- ")
            status = changebldgname(obldg, nbldg)
            if status:
                print("Building  name modified")
            else:
                print(f"no bldg found with {obldg}")

        case 7:
            displayall()
        case 8:
            nm = input("Enter name")
            lst = displaybyownername(nm)
            if lst != None:
                print(lst)
            else:
                print("Not Found")

        case 9:
            print("Thank you for Visiting us !!")
            exit(0)
        case _:
            print("Wrong Choice ? ?")
