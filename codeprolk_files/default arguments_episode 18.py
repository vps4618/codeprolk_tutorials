def details(student="vishwa",marks=89,subject="maths"):#vishwa,89,maths are defaullt arguments
    print(student)
    print(marks)
    print(subject)
details()    


def student(name,*friends):#(*) use for show that except first value ,other all values related to friends argument
    print(name)
    print(friends)
student("vishwa","mandipa","senula")    

#how to add dictionary in arguments
def student(name,marks,**friends):#(**) use for that
    print(name)
    print(friends)
student("vishwa",54,mandipa=68,senula=72)    

#using for loop for that
def student(name,**friends):
    print(name)
    for keys,values in friends.items():
        print(keys," = ",values)
student("vishwa",mandipa=54,senula=67)    
