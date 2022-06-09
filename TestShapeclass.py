from shapeclass import *

lst = []


def addnewshape(ch):
    id = input("input id ")
    c = input("enter color")
    if ch == 1:
        b = float(input("enter base:- "))
        h = float(input("enter height:- "))
        s1 = float(input("enter side1:- "))
        s2 = float(input("enter side2:- "))
        ob = Triangle(id, c, h, b, s1, s2)
    elif ch == 2:
        r = float(input("Enter Radius of circle:- "))
        ob = Circle(id, c, r)
    else:
        l = float(input("Enter length:- "))
        w = float(input("Enter width:- "))
    lst.append(ob)


def searchbyid(id):
    for ob in lst:
        if ob.get_id() == id:
            return ob
        else:
            return None


def findarea(id):
    ob = searchbyid(id)
    if ob != None:
        return ob.calcarea()
    else:
        return -1


def findperimeter(id):
    ob = searchbyid(id)
    if ob != None:
        return ob.calcperimeter()
    else:
        return -1


def countShapes():
    tcnt, ccnt, rcnt = 0, 0, 0
    for ob in lst:
        if isinstance(ob, Triangle):
            tcnt += 1
        elif isinstance(ob, Circle):
            ccnt += 1
        elif isinstance(ob, Rectangle):
            rcnt += 1
    return tcnt, ccnt, rcnt


def displayall():
    for ob in lst:
        print(ob)


choice = 0
while choice != 6:
    print('''
    1. add new shape
    2. count shape types
    3. calculation area by id
    4. calculate perimeter by id
    5. Display all
    6. exit
    ''')
    choice = int(input("Enter your choice :"))
    match choice:
        case 1:
            print("""1. Triangle \n 2. Circle \n 3.Rectangle""")
            ch = int(input("select shape"))
            addnewshape(ch)
        case 2:
            print("Count of Shapes is as follows:- ")
            cnt = countShapes()
            print(f"Triangles Count : {cnt[0]}")
            print(f"Circles Count : {cnt[1]}")
            print(f"Rectangles Count : {cnt[2]}")
        case 3:
            id = input("enter id ")
            print(findarea(id))
        case 4:
            id = input("enter id ")
            print(findperimeter(id))
        case 5:
            displayall()
        case 6:
            print("Thank you for visiting ")
            exit()
        case _:
            print("Wrong choice ")
