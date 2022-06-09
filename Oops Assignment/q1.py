from Songserviceclass import SongService

lst = []


def addnewsong():
    sid = int(input("Enter sid"))
    lyrics = (input("Enter lyrics"))
    singerName = (input("Enter singer name"))
    s = SongService(sid, lyrics, singerName)
    lst.append(s)


def searchbysingerName(singername):
    for idx, ob in enumerate(lst):
        if ob.get_singername() == singername:
            return ob, idx
    return None, -1


def display():
    for ob in lst:
        print(ob)
        print("_" * 40)


choice = 0
while choice != 4:
    print('''
    1.add new song
    2.Display all song
    3.display song by singer name
    4.exit
    ''')
    choice = int(input("enter your choice:- "))
    match choice:
        case 1:
            addnewsong()
        case 2:
            display()
        case 3:
            singerName = input("Enter Singer Name :- ")
            s, _ = searchbysingerName(singerName)
            if s is not None:
                print(s)
            else:
                print("not found")
        case 4:
            print("thanks for visiting")
            exit()
        case _:
            print("Wrong choice")
