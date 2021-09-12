#how to check whether a element present in a list or tuple
x=[1,2,3,4]
print(5 in x)
y=(1,2,3,4,5,6)
print(6 in y)

#for loops
a=[1,2,3,4,5,6]#num variable stands for each of the elements in list
for num in a:
    print(num)

#example 2
i={"name":"vishwa","age":"16","school":"Taxila Central College"}
for key in i.keys():#how to access to keys
    print(key)    
for values in i.values():#how to access to values
    print(values)

#1st method
for items in i.items():##how to access to both keys and values
    print(items)
#2nd method
for items,keys in i.items():##how to access to both keys and values
    print(items,keys)

#how to get rid of starting at 0
#for i in range(1,15):
#    print(i)    

#range function
#for range in range(10):
#    print(range)            

#how to make sequence
for sequence in range(2,20,2):
    print(sequence)        
    