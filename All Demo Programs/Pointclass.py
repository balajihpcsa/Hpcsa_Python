class Point:
    cnt = 1  # static variable

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        self.__id = Point.cnt
        Point.cnt = Point.cnt + 1

    def __str__(self):
        return f"ID: {self.__id} x: {self.__x} y:{self.__y}"

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.__x + other.__x
            y = self.__y + other.__y
        else:
            x = self.__x + other
            y = self.__y + other
        return Point(x, y)

    def __radd__(self, other):
        # if isinstance(other,Point):
        x = self.__x + other
        y = self.__y + other
        return Point(x, y)

    def __sub__(self, other):
        if isinstance(other, Point):
            x = self.__x - other.__x
            y = self.__y - other.__y
        return Point(x, y)

    def __mul__(self, other):
        if isinstance(other, Point):
            x = self.__x * other.__x
            y = self.__y * other.__y
        return Point(x, y)

    def __truediv__(self, other):
        if isinstance(other, Point):
            x = self.__x / other.__x
            y = self.__y / other.__y
        return Point(x, y)


# default constructor
p = Point()
p1 = Point(20, 10)
print(p)
print(p1)
print(f"count: {Point.cnt}")
p2 = Point(20, 30)
p3 = p1 + p2

print(p3)
p4 = p1 + p3
print(p4)  # add

# radd
p5 = 20 + p2
print(p5)

# subtraction
p6 = p1 - p2
print(p6)

# Multiplication
p7 = p1 * p2
print(p7)

# division
p8 = p1 / p2
print(p8)
