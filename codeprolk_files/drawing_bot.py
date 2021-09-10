import turtle,time,os,datetime

print("Loading........")
t=0
x=turtle.Turtle()
x.shape("turtle")
x.pu()
x.lt(90)
x.fd(300)



turtle.speed(00)
#first sun art
from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.speed(10)
time.sleep(1)
for i in range(1000):
    turtle.undo()

#SECOND sun art
turtle.speed(0)
from turtle import *
color('blue', 'pink')
begin_fill()
while True:
    forward(-200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.speed(10)
time.sleep(1)
for i in range(1000):
    turtle.undo()

#third sun art
turtle.speed(0)
from turtle import *
color('green', 'red')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.speed(10)
time.sleep(1)
for i in range(1000):
    turtle.undo()

#fourth sun art
turtle.speed(0)
from turtle import *
color('brown', 'orange')
begin_fill()
while True:
    forward(-200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.speed(10)
time.sleep(1)
for i in range(1000):
    turtle.undo()    

#fifth sun art
turtle.speed(0)
from turtle import *
color('purple', 'silver')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
turtle.speed(10)
time.sleep(1)
for i in range(1000):
    turtle.undo()


clear = lambda: os.system('cls')
clear()


print("-------------------------------------")
time1=datetime.datetime.today()
print(time1)
print("-------------------------------------")
print("Welcome to Drawing_bot !")

print("-------------------------")
print("            Instructions")
print("\n")
print("1.Type the names of colours correctly.")
print("\n")
print("2.Always type integer values when typing numbers.")
print("\n")
print("3.Type integers when asking directions and distances.")
print("\n")


x.reset()


turtle.speed(3)

x.pd()

p=input("Enter pen colour : ")
print("\n")
f=input("Enter fill colour : ")
print("\n")
x.color(p,f)
size=int(input("Enter pen size : "))
print("\n")
x.pensize(size)
screen=input("Enter background colour : " )
turtle.bgcolor(screen)
print("\n")
pen_up=input("Where to pull the pen ? (up-u , down-d) : ")
if pen_up=="u":
    x.penup()
else:
    x.pendown()    
print("\n")
hide=input("Do you want to hide the turtle ? (yes-y , no-n) : ")
if hide=="y":
    x.hideturtle()
else:
    x.showturtle()


while(t<100): 
             print("\n")
             s=input("Enter the shape (circle-c , line-l , dot-d) : ")
             print("\n")
             if s=="l":
                        i=input("Where to Move ? (forward-f, backward-b, left-l, right-r) : ")
                        print("\n")
                        if i=="f":
                                   a=float(input("Enter distance : "))
                                   
                        elif i=="l":
                                   b=float(input("Enter angle : "))
                                      
                        elif i=="b":
                                   c=float(input("Enter distance : "))
                                   
                        else:
                                   d=float(input("Enter angle : "))
                                   
                        print("\n")                                                           
             
                        if i=="f":
                                  x.forward(a)
                             
                        elif i=="l":
                                  x.left(b)
                        elif i=="b":
                                   x.back(c)
                        else:
                             x.right(d)             
             elif s=="c":
                 i=float(input("Enter radius of the circle : "))
                 print("\n")
                 x.circle(i)
             else:
                 i=int(input("Enter size of the dot : "))
                 print("\n")
                 co=input("Enter colour of the dot : ")
                 print("\n")
                 x.dot(i,co)

             q=input("Do you want to change colour of pen and other items (yes-y ,no-n) ? : ")
             print("\n")
             if q=="y":
                       p=input("Enter pen colour : ")
                       print("\n")
                       f=input("Enter fill colour : ")
                       print("\n")
                       x.color(p,f)
                       size=int(input("Enter pen size : "))
                       print("\n")
                       turtle.pensize(size)
                       screen=input("Enter background colour : " )
                       print("\n")
                       turtle.bgcolor(screen)
                       pen_up=input("Where to pull the pen ? (up-u , down-d) : ")
                       print("\n")
                       if pen_up=="u":
                                       x.penup()
                       else:
                             x.pendown()
                       
                       hide=input("Do you want to hide the turtle ? (yes-y , no-n) : ")
                       print("\n")
                       if hide=="y":
                                    x.hideturtle()
                       else:
                             x.showturtle()
                       shape1=input("Do you want to change the turtle to another shape ? (yes-y , no-n) : ")
                       if shape1=="y":
                           print("\n")
                           shape2=input("Enter shape (circles,square,triangle): ")

                           x.shape(shape2)
                       else:
                           time.sleep(0.00000000000001)
                       print("\n")              
                       t_size=input("Do you want to change size of the turtle ? (yes-y , no-n) : ")
                       if t_size=="y":
                           print("\n")
                           width1=float(input("Enter width of the turtle : "))
                           print("\n")
                           length1=float(input("Enter length of the turtle : "))
                           x.turtlesize(width1,length1)
                           print("\n")
                       else:
                           time.sleep(0.000000000000001)
                       print("\n")    
                       speed1=input("Do you want to speedup the turtle ? (yes-y , no-n) : ")

                       if speed1=="y":
                                  print("\n")
                                  speed2=int(input("Enter the speed (Fastest-0 ,Fast-10 ,Normal-6 ,Slow-3 ,Slowest-1) : "))
                                  x.speed(speed2)
                       else:
                            time.sleep(0.00000000000000001)
                            print("\n")

                       
                       
                       
             else:
                 time.sleep(0.0000000000000001)
             
             options=input("Do you want see options ? (yes-y , no-n) : ")
             if options=="y":
                              print("\n")
                              undo=input("Do you want to undo any action ? (yes-y , no-n) : ")

                              if undo=="y":
                                           print("\n")
                                           undo_size=int(input("Enter the number of actions do you want to undo : "))
                                           for z in range(undo_size):
                                            x.undo()
                              else:
                                   time.sleep(0.0000000000000001)        
                              print("\n")
             
                              fill=input("Do you want to start filling shapes ? (yes-y , no-n) : ")
             
                              if fill=="y":
                                           x.begin_fill()
                                           fi=0
                 
                                           print("\n")
                                           p=input("Enter pen colour : ")
                                           print("\n")
                                           f=input("Enter fill colour : ")
                                           print("\n")
                                           x.color(p,f)
                                           size=int(input("Enter pen size : "))
                                           x.pensize(size)
                 
                                           while(fi<100):
                                                       print("\n")
                                                       s=input("Enter the shape (circle-c , line-l) : ")
                                                       print("\n")
                                                       if s=="l":
                                                                 i=input("Where to Move ? (forward-f, backward-b, left-l, right-r) : ")
                                                                 print("\n")
                                                                 if i=="f":
                                                                     a=float(input("Enter distance : "))
                                   
                                                                 elif i=="l":
                                                                      b=float(input("Enter angle : "))
                                      
                                                                 elif i=="b":
                                                                      c=float(input("Enter distance : "))
                                   
                                                                 else:
                                                                     d=float(input("Enter angle : "))
                                   
                                                                 print("\n")                                                           
             
                                                                 if i=="f":
                                                                      x.forward(a)
                             
                                                                 elif i=="l":
                                                                       x.left(b)
                                                                 elif i=="b":
                                                                       x.back(c)
                                                                 else:
                                                                      x.right(d)             
                                                       else: 
                                                             i=float(input("Enter radius of the circle : "))
                                                             print("\n")
                                                             x.circle(i)
                                                       q=input("Do you want to change colour of pen and other items (yes-y ,no-n) ? : ")
                                                       print("\n")
                                                       if q=="y":
                                                             p=input("Enter pen colour : ")
                                                             print("\n")
                                                             f=input("Enter fill colour : ")
                                                             print("\n")
                                                             x.color(p,f)
                                                             size=int(input("Enter pen size : "))
                                                             print("\n")
                                                             turtle.pensize(size)
                                                       else:
                                                           time.sleep(0.0000000000000001)
                                                       e=input("Do you want to end filling shapes ? (yes-y ,no-n ) : ")
                                                       if e=="n":
                                                            time.sleep(0.0000000000000001)
                                                       else:
                                                          x.end_fill()
                                                       print("\n")    
                                                       e=input("Do you want to exit this filling shapes ? (yes-y ,no-n ) : ")
                                                       if e=="n":
                                                           time.sleep(0.0000000000000001)
                                                       else:
                                                           break     
                              else:
                                  time.sleep(0.0000000000000000001)                   

                              print("\n")
                              reset1=input("Do you want clear all drawings ? (yes-y , no-n) : ")
                              if reset1=="y":
                                         x.clear()
                              else:
                                 time.sleep(0.000000000000001)    
                       
                              print("\n")
                              e=input("Do you want to exit this programme ? (yes-y ,no-n ) : ")
                              if e=="n":
                                   time.sleep(0.0000000000000001)
                              else:
                                   break
             else:
                 time.sleep(0.000000000000000001)                    


