from studentclass import *

lst = {Student(1, "balaji", "HPCSA@.com", 80, 90, 99), Student(2, "Pratik", "HPCSA@.com", 85, 85, 90)}


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
    if studid != -1:
        return studid.calculategpa()
    else:
        return "Not Found"


choice = 0


def addnewstudent():
    try:
        sid = int(input("Enter Student Id:- "))
        if sid >= 0 and len(sid) >= 4:
            raise ValueError
        sname = input("Enter Student Name:- ")
        semail = input("Enter Student Email:- ")
        m1 = int(input("Enter Student Marks1:- "))
        m2 = int(input("Enter Student Marks2:- "))
        m3 = int(input("Enter Student Marks3:- "))

    except:
        print("exception")


while choice != 5:
    print('''
        1.
        2. Display All Student
        3. Search by id
        4. Search by name
        5. calculate GPA of a student
        6. Exit
    ''')
    choice = int(input("Enter your choice :"))
    match choice:
        case 1:
            addnewstudent()
        case 2:
            displayall()
        case 3:
            sid = int(input("Enter Student Id :- "))
            status = searchbyid(sid)
            if status != -1:
                print(status)
            else:
                print("Not Found")
        case 4:
            name = input("Enter Student Name :- ")
            print(searchbyname(name))
        case 5:
            id = int(input("Enter Student Id :- "))
            print(calculategpa(id))
        case 6:
            print("Thank you for visiting ")
            exit()
        case _:
            print("Wrong choice ")
