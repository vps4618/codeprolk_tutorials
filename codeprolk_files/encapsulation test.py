class myclass:
    def meth1(self):
        print("hello")
        self.__meth2()
    def __meth2(self):
        print("welcome")
phone=myclass()
phone.meth1()