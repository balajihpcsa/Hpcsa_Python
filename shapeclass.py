from abc import abstractmethod, ABC


class Shape(ABC):
    def __init__(self, id=1, color="white"):
        self.__id = id
        self.__color = color

    def __str__(self):
        return f"id : {self.__id} color: {self.__color} "

    def set_id(self, id):
        self.__id = id

    def set_color(self, color):
        self.__color = color

    def get_id(self):
        return self.__id

    def get_color(self):
        return self.__color

    @abstractmethod
    def calcarea(self):
        pass

    @abstractmethod
    def calcperimeter(self):
        pass


class Triangle(Shape):
    def __init__(self, id, color, h, b, s1, s2):
        super().__init__(id, color)
        self.__height = h
        self.__base = b
        self.__s1 = s1
        self.__s2 = s2

    def __str__(self):
        return super().__str__() + f" base :{self.__base} Height: {self.__height} side1:{self.__s1} side2:{self.__s2}"

    def set_base(self, base):
        self.__base = base

    def set_height(self, height):
        self.__height = height

    def set_s1(self, s1):
        self.__s1 = s1

    def set_s2(self, s2):
        self.__s2 = s2

    def get_base(self):
        return self.__base

    def get_height(self):
        return self.__height

    def get_s1(self):
        return self.__s1

    def get_s2(self):
        return self.__s2

    def calcarea(self):
        return 0.5 * self.__base * self.__height

    def calcperimeter(self):
        return self.__base + self.__s1 + self.__s2


class Circle(Shape):
    def __init__(self, id, color, r):
        super().__init__(id, color)
        self.__r = r

    def __str__(self):
        return super().__str__() + f" Radius :{self.__r}"

    def set_r(self, r):
        self.__r = r

    def get_r(self):
        return self.__r

    def calcarea(self):
        return 3.14 * self.__r * self.__r

    def calcperimeter(self):
        return 2 * 3.14 * self.__r


class Rectangle(Shape):
    def __init__(self, id, color, l, w):
        super().__init__(id, color)
        self.__l = l
        self.__w = w

    def __str__(self):
        return super().__str__() + f" Length :{self.__l} Breadth : {self.__w}"

    def set_l(self, l):
        self.__l = l

    def set_b(self, w):
        self.__w = w

    def get_l(self):
        return self.__l

    def get_b(self):
        return self.__w

    def calcarea(self):
        return self.__l * self.__w

    def calcperimeter(self):
        return 2 * (self.__l + self.__w)


if __name__ == "__main__":
    t = Triangle(1, "red", 5, 5, 4, 3)
    c = Circle(1, "Red", 4)
    r = Rectangle(1, "Red", 10, 2)

    print(f"{t} \n  Area : {t.calcarea()} \n Perimeter : {t.calcperimeter()}\n {'-' * 70}")

    print(f"{c} \n  Area : {c.calcarea()} \n Perimeter : {c.calcperimeter()}\n {'-' * 70}")

    print(f"{r} \n  Area : {r.calcarea()} \n Perimeter : {r.calcperimeter()}\n {'-' * 70}")
