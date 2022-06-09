'''
'''
Vdictionary = {'Balaji': ['ferrari', 'bugati'], 'Pratik': ['Bmw', 'kawasaki']}
vlist = []


def addnewperson():
    name = input("Enter Name of Person:- ")
    ch = 'y'
    while ch != 'n':
        vehicle = input("Enter vehicle:- ")
        vlist.append(vehicle)
        ch = input("Do you want to continue(y/n) :- ")
    Vdictionary[name] = vlist
    return True


def deleteperson():
    name = input("Enter Name of person To be deleted:- ")
    check = Vdictionary.get(name, -1)
    if (check != -1):
        print(f"Name Of person {name} and Vehicles are :- {Vdictionary.get(name)} ")
        ch = input("Do you want to delete(y/n):- ")
        if (ch == 'y'):
            Vdictionary.pop(name)
            return 1
        else:
            return 2
    else:
        return 3


def modifyperson():
    name = input("Enter Name of person To be modified:- ")
    check = Vdictionary.get(name, -1)
    if (check != -1):
        print(f"Name Of person {name} and Vehicles are :- {Vdictionary.get(name)} ")
        ch = input("Do you want to modify(y/n):- ")
        if (ch == 'y'):
            ovch = input("Enter vehicle name to modify:- ")
            nvch = input("Enter new Vehicle  name:- ")
            pos = Vdictionary.get(name).index(ovch)
            Vdictionary[name][pos] = nvch
            return 1
        else:
            return 2
    else:
        return 3


def searchperson():
    name = input("Enter Name of person :- ")
    check = Vdictionary.get(name, -1)
    if (check != -1):
        print(f"Name Of person {name} and Vehicles are :- {','.join(Vdictionary.get(name))} ")
    else:
        print("Person Not Found")


def searchbyvehicle():
    vname = input("Enter Name Vehicle :- ")
    blist = []
    for k, v in Vdictionary.items():
        if vname in v:
            blist.append(k)
    if len(blist) == 0:
        return None
    else:
        return blist


def displayallperson():
    print(f"Name of person are as follows {','.join( Vdictionary.keys())} ")


def displayallvehicles():
    s=set()
    #for v in Vdictionary.values():
    #    for i in len
    #    s.add(v)
    res = list(map(','.join, Vdictionary.values()))
    print(f"Name of Vehicles are {','.join(res)}  ")

'''
Write a menu driven program to practice Vdictionaryionary functions.
Write a program to accept name of a person and their vehicle and store it in a Vdictionaryionary.
Ask user if they want to continue to accept multiple values.
Display following menu:
1. Add new person name and a vehicle name.
2. Delete a person name and vehicle name from the Vdictionaryionary.
----Accept person name from user.
----Check whether person name exists in the Vdictionaryionary.
----If exists show person name and vehicle name to the user.
----Confirm for deletion, if user enters y
then delete otherwise no. Display appropriate message.
3. Modify vehicle name for the person
----Accept a person name from user.
----Check whether the person’s name exists.
----If the name exists, show the person’s name and vehicle name to user.
Ask for new value and then overwrite the old value.
4. Search vehicle for the given person’s name.
5. Search list of people, who have given a vehicle
6. Display all person names.
7. Display all vehicle names.
8 Exit
'''

choice = 0
while choice != 8:
    print("""
            1. Add new person name and a vehicle name.
            2. Delete a person name and vehicle name from the Vdictionaryionary.
            3. Modify vehicle name for the person
            4. Search vehicle for the given person’s name.
            5. Search list of people, who have given a vehicle
            6. Display all person names.
            7. Display all vehicle names.
            8 Exit
            """)
    choice = int(input("Enter Your Choice:- "))
    match choice:
        case 1:
            status = addnewperson()
            if status == True:
                print("New Person and vehicle added!!")
        case 2:
            status = deleteperson()
            if status == 1:
                print("Person Deleted")
            elif status == 2:
                print("Person Found But not deleted")
            elif status == 3:
                print("Person not Found")
        case 3:
            status = modifyperson()
            if status == 1:
                print("Person Modified")
            elif status == 2:
                print("Person Found But not Modified")
            elif status == 3:
                print("Person not Found")
        case 4:
            status = searchperson()
            if status != None:
                print(f"Name Of person are :- {','.join(status)} ")

        case 5:
            status = searchbyvehicle()
            if status != None:
                print(f"Name Of person are :- {','.join(status)} ")

        case 6:
            displayallperson()
        case 7:
            displayallvehicles()
        case 8:
            print("Thank you for Visiting us !!")
            exit(0)
        case _:
            print("Wrong Choice ? ?")
