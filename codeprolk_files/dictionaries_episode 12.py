from typing import OrderedDict


x={"physics":84,
   "maths":79,
   "chemistry":62}
print(x)
#elements [physics,maths,chemistry] are known as keys.
# elements [64,79,62] are known as values assigned to keys.

#how to access to values in keys
print(x["chemistry"])
print(x["maths"])
print(x["physics"])

#example 2
y={"name":"vishwa",
   5:3,
   (3,4):45,
   True:4}
print(y)

#how to find length
print(len(y))

#how to add key or value to the dictionary
y["age"]=16
print(y)

#how to remove a keyvalue
y.pop(True)
print(y)

#how to clear dictionary
# y.clear()
# print(y)

#how to delete dictionary
# del y
# print(y)

#how to change elements in dictionaries
y["name"]="praveen"
print(y)

#how to print only keys
print(y.keys())

#how to print only values
print(y.values())

#how to print both keys and values
print(y.items())