clist = []
choice = 0


def addnewcourse():
    course = input("Enter Course Name:-  ")
    clist.append(course)


def deletecourse(course):
    if course in clist:
        ans = input(f"Do you want to Delete {course} press Y :-  ")
        if ans == "Y":
            clist.remove(course)
            return 1
        else:
            return 2
    return 3


def modifycourse(old, new):
    if old in clist:
        pos = clist.index(old)
        ans = input(f"Do you want to Modify {old} to {new} press Y :-  ")
        if ans == "Y":
            clist[pos] = new
            return 1
        else:
            return 2
    return 3


def displaycourseendswithA(substr):
    cnt = 1
    for c in clist:
        if c.endswith(substr):
            print(f"{cnt}: {c}")
            cnt = cnt + 1


def displayall(lst=clist):
    cnt = 1
    for c in lst:
        print(f"{cnt}: {c}")
        cnt = cnt + 1


def displaysort(order):
    ccopy = clist.copy()
    if order.lower() == "a":
        ccopy.sort()
    else:
        ccopy.sort(reverse=True)
    displayall(ccopy)


def searchbyname(course):
    if course in clist:
        pos = clist.index(course)
        return pos
    else:
        return -1


while choice != 8:
    print('''
    1. add new course
    2. delete the course
    3. modify course
    4. display all
    5. display course names ends with A
    6. display all alphabetically
    7. search by name
    8. exit
    ''')
    choice = int(input("Enter Your Choice :- "))
    match choice:
        case 1:
            addnewcourse()
        case 2:
            status = deletecourse(input("Enter The course name to delete :- "))
            if status == 1:
                print("deleted successfully")
            elif status == 2:
                print("Found but Not deleted")
            elif status == 3:
                print("Not Found")
        case 3:
            old = input("Enter the old Course name to modify :- ")
            new = input("Enter the new Course :- ")
            status = modifycourse(old, new)
            if status == 1:
                print("Modified successfully")
            elif status == 2:
                print("Found but Not Modified")
            elif status == 3:
                print("Not Found")
        case 4:
            displayall()
        case 5:
            displaycourseendswithA("A")
        case 6:
            order = input("Enter A for Ascending or D For Descending:- ")
            displaysort(order)
        case 7:
            course = input("Enter Course to Search :- ")
            pos = searchbyname(course)
            if pos != -1:
                print(f"Found at {pos}: {course}")
            else:
                print("Not Found")
        case 8:
            print("Thank You For visiting !!!!")
        case _:
            print("Wrong Choice ? ?")
