x=int(input("Enter the value that you want to find its factorial : "))
# 4!=1*2*3*4=24
# 4!=4*3*2*1=24
result=1
print("------------------------------------------------------")
for i in range(1,x+1):
    result=result*i
print(f'Factorial value of {x} is {result}.')    

