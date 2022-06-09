class A:
    def __init__(self, a1=0, a2=0):
        self.__a1 = a1
        self.__a2 = a2

    def __str__(self):
        return f"A1:{self.__a1} A2:{self.__a2}"


class B(A):
    def __init__(self, b1, b2, **kwargs):
        print("in B", kwargs)
        super().__init__(**kwargs)
        self.__b1 = b1
        self.__b2 = b2

    def __str__(self):
        return super().__str__() + f" B1:{self.__b1} B2:{self.__b2}"


class C(A):
    def __init__(self, c1, **kwargs):
        print("in C", kwargs)
        super().__init__(**kwargs)
        self.__c1 = c1

    def __str__(self):
        return super().__str__() + f" C1:{self.__c1}"


class D(B, C):
    def __init__(self, d1, d2, **kwargs):
        print("in D", kwargs)
        super().__init__(**kwargs)
        self.__d1 = d1
        self.__d2 = d2

    def __str__(self):
        return super().__str__() + f" D1:{self.__d1} D2:{self.__d2}"


if __name__ == "__main__":
    ob = D(a1=10, b1=21, b2=25, c1=31, d1=31, d2=32)
    print(ob)
    print(D.mro())
