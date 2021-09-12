def divide(x,y):
    return x/y
print(divide(0,5))

def divide(x,y):
    return x/y
# print(divide(5,0))
# generates an error(5 can't divide by 0)

#how to prevent from this error message
def divide(x,y):
    if y==0:
        x,y=y,x
    return x/y
print(divide(5,0))

#how to use decorator to prevent from this error message
def new(func):#decorator
    def inside(x,y):
        if y==0:
            x,y=y,x
        return func(x,y)
    return inside   

# how to connect decorator with function

@new #way  to connect(method 2)

def divide1(x,y):
    return x/y

divide1=new(divide1) #way to connect(method 1)
print(divide1(9,0))        
                 
    
        