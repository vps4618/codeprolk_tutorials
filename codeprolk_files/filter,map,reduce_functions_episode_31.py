# filter function
number=[1,2,3,4,5,6,7,8]
def even_num(x):
    return x%2==0
y=list(filter(even_num,number))
print(y)    

def odd_num(x):
    return x%2==1
y=list(filter(odd_num,number))
print(y)    

y=list(filter(lambda x:x%2==0,number))
print(y)    

#map function
y=list(map(lambda x:x*2,number))
print(y)

y=list(map(lambda x:x-2,number))
print(y)

#reduce function

from functools import reduce
sum=reduce(lambda x,y:x+y,number)
print(sum)
multi=reduce(lambda x,y:x*y,number)
print(multi)