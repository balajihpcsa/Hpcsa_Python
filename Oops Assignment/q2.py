from studentclass import *

lst = {Student(1, "balaji", "HPCSA", 80, 90, 99), Student(2, "Pratik", "HPCSA", 85, 85, 90)}


def displayall():
    for ob in lst:
        print(ob, "\n", "-" * 70)


def searchbyid(sid):
    for ob in lst:
        if sid == ob.get__sid():
            return ob
        else:
            return -1


def searchbyname(sname):
    for ob in lst:
        if sname == ob.get__snm():
            return ob
        else:
            return "Not Found"

def calculategpa(sid):
    studid = searchbyid(sid)
    if studid!=-1:
        return studid.calculategpa()
    else:
        return "Not Found"


choice = 0
while choice != 5:
    print('''
        1. Display All Student
        2. Search by id
        3. Search by name
        4. calculate GPA of a student
        5. Exit
    ''')
    choice = int(input("Enter your choice :"))
    match choice:
        case 1:
            displayall()
        case 2:
            sid = int(input("Enter Student Id :- "))
            status=searchbyid(sid)
            if status!=-1:
                print(status)
            else:
                print("Not Found")
        case 3:
            name = input("Enter Student Name :- ")
            print(searchbyname(name))
        case 4:
            id = int(input("Enter Student Id :- "))
            print(calculategpa(id))
        case 5:
            print("Thank you for visiting ")
            exit()
        case _:
            print("Wrong choice ")
