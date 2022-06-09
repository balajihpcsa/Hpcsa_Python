''''''
'''
Q3. Write a python program to store information of your friends
id,name,lastname,hobbies,mobno,email,bdate,address
note: hobbies- a friend may have multiple hobbies

Accept all friends details and store it in a list
And do the following.
1. Display All Friend
2. Search by id
3. Search by name
4. Display all friend with a particular hobby
5. Exit
'''


class StudentWithHobbies:
    def __init__(self, sid, sname, slname, hobbies=[], mobno=12345, email="demo@demo.com", bdate="01-01-1991",
                 address="Local"):
        self.__sid = sid
        self.__sname = sname
        self.__slname = slname
        self.__hobbies = hobbies
        self.__mobno = mobno
        self.__email = email
        self.__bdate = bdate
        self.__address = address

    def __str__(self):
        return f"Id:- {self.__sid},\n Name:- {self.__sname},\n Lastname:- {self.__slname},\n " \
               f"Hobbies:- {','.join(self.__hobbies)},\n Mobno:- {self.__mobno},\n email:- {self.__email},\n " \
               f"Bdate:- {self.__bdate},\n Address:- {self.__address}"

    def set__sid(self, sid):
        self.__sid = sid

    def set__sname(self, sname):
        self.__sname = sname

    def set__slname(self, slname):
        self.__slname = slname

    def set__hobbies(self, hobbies):
        self.__hobbies = hobbies

    def set__mobno(self, mobno):
        self.__mobno = mobno

    def set__email(self, email):
        self.__email = email

    def set__bdate(self, bdate):
        self.__bdate = bdate

    def set__address(self, address):
        self.__address = address

    def get__sid(self):
        return self.__sid

    def get__sname(self):
        return self.__sname

    def get__slname(self):
        return self.__slname

    def get__hobbies(self):
        return self.__hobbies

    def get__mobno(self):
        return self.__mobno

    def get__email(self):
        return self.__email

    def get__bdate(self):
        return self.__bdate

    def get__address(self):
        return self.__address


if __name__ == "__main__":
    s = StudentWithHobbies(1, "Pratik", "Dolas", ["reading", "Swimming", "trek"], 65412, "pratik@pratik.com",
                           "28-08-1996", "Mahad")
    print(s)
