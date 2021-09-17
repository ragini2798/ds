class pyclass:
    __personal = "private"
    __professional ="private"
    __financial = "private"
    def __m1(self):
        print("this is private method")
        print(pyclass.__personal)

    def __m2(self):
         print("this is private method")
         print(pyclass.__professional)

    def __m3(self):
         print("this is private method")
         print(pyclass.__financial)

    def dummy(self):
        self.__m1()

    def dummy1(self):
        self.__m2()

    def dummy2(self):
        self.__m3()

class oops(pyclass):
    def m4(self):
        self.dummy()
    def m3(self):
        self.dummy()

obj = oops()
obj.m4()
obj.m3()
