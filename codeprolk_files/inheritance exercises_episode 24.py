class parent:
    def func1(self):
        print("hello")
class child(parent):
    def func2(self):
        print("welcome")
myobj=child()
myobj.func1()
myobj.func2()

#how to call both two functions in two classes at once(for that we use super function)
class parent1:
    def func3(self):
        print("hello")
class child1(parent1):
    def func4(self):
        print("welcome")
        super().func3()
myobj1=child1()
myobj1.func4()

#method overwriting
#inthis method func5 is overwrited in child2 class
class parent2:
    def func5(self):
        print("bye")
class child2(parent2):
    def func6(self):
        print("come")
    def func5(self):
        print("go")
myobj2=child2()
myobj2.func5()

print("________________________")
print("fruit shop")
print(" ")

#exercise 1

class fruits:
    number_of_items=None
    unit_price=None
    def set_value(self,x,y):
        self.number_of_items=x
        self.unit_price=y
class Apple(fruits):
    def price(self):
        print("Price for Apples is Rs.",self.number_of_items*self.unit_price,".")
class Orange(fruits):
    def price(self):
        print("Price for Oranges is Rs.",self.number_of_items*self.unit_price,".")
class Grapes(fruits):
    def price(self):
        print("Price for Grapes is Rs.",self.number_of_items*self.unit_price,".")
class Mango(fruits):
    def price(self):
        print("Price for Mangoes is Rs.",self.unit_price*self.number_of_items,".")
bill1=Apple()
bill2=Orange()
bill3=Grapes()
bill4=Mango()

bill1.set_value(10,20)
bill2.set_value(20,30)
bill3.set_value(30,4)
bill4.set_value(10,50)

bill1.price()
bill2.price()
bill3.price()
bill4.price()