from abc import abstractmethod, ABC


class Person:
    def __init__(self, pid, name, mob):
        self.__pid = pid
        self.__name = name
        self.__mob = mob

    def __str__(self):
        return f" Id : {self.__pid}\n Name :- {self.__name}\n Mob no:- {self.__mob}\n "

    def set_pid(self, pid):
        self.__pid = pid

    def set_name(self, name):
        self.__name = name

    def set_mob(self, mob):
        self.__mob = mob

    def get_pid(self):
        return self.__pid

    def get_name(self):
        return self.__name

    def get_mob(self):
        return self.__mob


class Employee(Person, ABC):

    def __init__(self, pid, name, mob, desg, dept):
        super().__init__(pid, name, mob)
        self.__desg = desg
        self.__dept = dept

    def __str__(self):
        return super().__str__() + f"Desg: {self.__desg}\n Dept:{self.__dept} "

    def set_dept(self, dept):
        self.__dept = dept

    def set_desg(self, desg):
        self.__desg = desg

    def get_desg(self):
        return self.__desg

    def get_dept(self):
        return self.__dept

    @abstractmethod
    def calculatesal(self):
        pass


class SalaryEmployee(Employee):
    def __init__(self, pid, name, mob, desg, dept, sal, bonus):
        super().__init__(pid, name, mob, desg, dept)
        self.__sal = sal
        self.__bonus = bonus

    def __str__(self):
        return super().__str__() + f"Sal: {self.__sal}\n Bonus:{self.__bonus} "

    def set_sal(self, sal):
        self.__sal = sal

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_sal(self):
        return self.__sal

    def get_bonus(self):
        return self.__bonus

    def calculatesal(self):
        return self.__sal + self.__bonus


class ContractEmployee(Employee):
    def __init__(self, pid, name, mob, desg, dept, hr_charges, no_ofhrs):
        super().__init__(pid, name, mob, desg, dept)
        self.__hr_charges = hr_charges
        self.__no_ofhrs = no_ofhrs

    def __str__(self):
        return super().__str__() + f" Charges: {self.__hr_charges}\n Hours Worked:{self.__no_ofhrs} "

    def set_hr_charges(self, hr_charges):
        self.__hr_charges = hr_charges

    def set_no_ofhrs(self, no_ofhrs):
        self.__no_ofhrs = no_ofhrs

    def get_hr_charges(self):
        return self.__hr_charges

    def get_no_ofhrs(self):
        return self.no_ofhrs

    def calculatesal(self):
        return self.__hr_charges * self.__no_ofhrs * 30


class Customer(Person):
    def __init__(self, pid, name, mob, type_of_member, charges):
        super().__init__(pid, name, mob)
        self.__type_of_member = type_of_member
        self.__charges = charges

    def __str__(self):
        return super().__str__() + f"Type of Member: {self.__type_of_member}\n Charges:{self.__charges} "

    def set_type_of_member(self, type_of_member):
        self.__type_of_member = type_of_member

    def set_charges(self, charges):
        self.__charges = charges

    def get_type_of_member(self):
        return self.__type_of_member

    def get_charges(self):
        return self.__charges


if __name__ == "__main__":
    semp = SalaryEmployee(1, "balaji", 12345, "Devloper", "IT", 25000, 5000)
    cemp = ContractEmployee(2, "Pratik", 67891, "Admin", "Support", 2000, 4)
    cust = Customer(3, "Anuj", 25014, "Helper", 6000)

    print(semp, "\n", "-" * 70)
    print(cemp, "\n", "-" * 70)
    print(cust, "\n", "-" * 70)

    print(semp.calculatesal(), "\n", "-" * 70)
    print(cemp.calculatesal(), "\n", "-" * 70)
