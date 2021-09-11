import random

def guess_number():
    hidden_number=random.randint(1,20)
    your_input=0
    while your_input!=hidden_number: # (!=) this is not equal operator
                   your_input=int(input("Enter number : "))
                   if your_input<hidden_number:
                            print("Too low ! Try again.")
                   if your_input>hidden_number:
                            print("Too high ! Try again.")
    print("You won !")

guess_number()
