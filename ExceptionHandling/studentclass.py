class Student:
    gpa = float(0)

    def __init__(self, sid, snm, email, m1, m2, m3):
        self.__sid = sid
        self.__snm = snm
        self.__email = email
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3

    def __str__(self):
        return f" SId : {self.__sid} \n Name : {self.__snm} \n Email : {self.__email} \n Marks 1 : {self.__m1} \n " \
               f"Marks 2 : {self.__m2} \n Marks 3 : {self.__m3}"

    # Setter Methods
    def set__sid(self, sid):
        self.__sid = sid

    def set__snm(self, snm):
        self.__snm = snm

    def set__email(self, email):
        self.__email = email

    def set__m1(self, m1):
        self.__m1 = m1

    def set__m2(self, m2):
        self.__m2 = m2

    def set__m3(self, m3):
        self.__m3 = m3

    def get__sid(self):
        return self.__sid

    def get__snm(self):
        return self.__snm

    def get__email(self):
        return self.__email

    def get__m1(self):
        return self.__m1

    def get__m2(self):
        return self.__m2

    def get__m3(self):
        return self.__m3

    def calculategpa(self):
        gpa = round(((1 / 3) * self.__m1 + (1 / 2) * self.__m2 + (1 / 4) * self.__m3), 2)
        return gpa


if __name__ == "__main__":
    p = Student(1, "balaji", "HPCSA@.com", 80, 90, 99)
    print(p.calculategpa())
    print(p)
