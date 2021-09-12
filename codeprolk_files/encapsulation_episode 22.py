#private variable
class myClass:
    x=10
    __y=20;#(__)use for define private variables(can't access from outer side of the class)


myObject=myClass()
print(myObject.x)
# print(myObject.__y)


#how to access to private variables
class myClass:
    x=10
    __y=20;#(__)use for define private variables(can't access from outer side of the class)
    def disp(self):
        return self.__y

myObject=myClass()
print(myObject.disp())

#private methods
class myclass:
    def meth1(self):
        print("hello")
    def __meth2(self):#to create private method we also use two underscores(__)
        print("welcome")

phone=myclass()
phone.meth1()
#phone.__meth2()


#how to access to private methods
class myclass:
    def meth1(self):
        print("hello")
        self.__meth2()
        
        
    def __meth2(self):#to create private method we also use two underscores(__)
        print("welcome")

phone=myclass()
phone.meth1()