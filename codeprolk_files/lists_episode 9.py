#examples for lists
x=[4,5,8,9,6,7]
y=['a','b','e','c','d']
z=[5,3.5,'c','python',True,[1,2,3]]

#how to access to a list's  elements
print(z[5])
print(z[3])

#how to change a element in a list
x[0]=12
print(x)

#finding length of a list using a inbuilt function called (len)
print(len(x))
print(len(z))

#adding elements to a list
x.insert(3,20)#inthis firstly,index number should be given
print(x)
x.append(50)#in thin no need of index number
print(x)

#how to remove elements from a list
x.remove(7)#use to remove specific element
print(x)
x.pop()#use to remove last element
print(x)

#how to remove all full elements in the list and list
# del x
# print(x)

#how to clear only all elements in the list
# x.clear()
# print(x)

#how to sort list elements in ascending order
y.sort()
print(y)

x.sort()
print(x)

#how to sort list elements in descending order
y.sort(reverse=True)
print(y)

x.sort(reverse=True)
print(x)

#how to assign elements in a list to lot of varibles
a,b,c,d=[1,2,3,4]
print(a)
print(b)
print(c)
print(d)

#how to assign elements in a list to different variables when their are not enough elements
#first example
e,f,*g=[5,6,7,8,9]#when this situation we use(*) 
print(e)
print(f)
print(g)

#second example
e,*f,g=[5,6,7,8,9]#when this situation we use(*) 
print(e)
print(f)
print(g)

#third example
*e,f,g=[5,6,7,8,9]#when this situation we use(*) 
print(e)
print(f)
print(g)
