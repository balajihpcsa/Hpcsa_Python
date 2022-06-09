class Person:
    def __init__(self, pid, pnm, mob):
        print("in person init")
        self.__pid = pid
        self.__pnm = pnm
        self.__mob = mob

    def __str__(self):
        return f" Id : {self.__pid} \n Name : {self.__pnm} \n Mobile : {self.__mob}"

    # Setter Methods
    def set_pid(self, pid):
        self.__pid = pid

    def set_pnm(self, pnm):
        self.__pnm = pnm

    def set_mob(self, mob):
        self.__mob = mob

    # getter Methods
    def get_pid(self):
        return self.__pid

    def get_pname(self):
        return self.__pnm

    def get_mob(self):
        return self.__mob


if __name__ == "__main__":
    p = Person(11, "balaji", 123456)
    print(p)
