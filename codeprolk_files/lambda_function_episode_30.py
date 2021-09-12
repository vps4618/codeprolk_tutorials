# lambda function can't use for functions with lot of steps
#lambda function==anonymous function
#creating lambda function for calculate area of the square

area=lambda x :x*x
perimeter=lambda x,y:2*x+2*y

print(perimeter(10,20))
print(area(10))

def apples(cost_price):
    return (lambda number_of_apples:cost_price*number_of_apples)
x=apples(20)
print(x(10))    