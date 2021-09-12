#example 1
class phone1:#parent class(super class)
    def feature1(self):
        print("camera")
class phone3:#parent class
    def feature3(self):
        print("blutooth")
class phone2(phone1,phone3):#child class(sub class) #to inherit we use infront of child class brackets and we input parent class in it
    def feature2(self):#multiple inheritance
        print("internet")
samsung=phone2()
#how to call a method in parent class
samsung.feature1()
samsung.feature3()
samsung.feature2()

#example 2(multi level inheritance)
class phone4:
    def feature4(self):
        print("camera")
class phone6(phone4):
    def feature6(self):
        print("blutooth")
class phone5(phone6):#in this class,both phone1 and phone3 are inherited because,previously phone4 class is inherited to phone6
    def feature5(self):
        print("internet")
apple=phone5()

apple.feature4()
apple.feature5()
apple.feature6()
