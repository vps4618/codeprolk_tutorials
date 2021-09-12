# 4!=4*3*2*1
# 4!=4*3!
# 4!=4*(4-1)!
# n!=n*(n-1)!
# 0!=1
#recursion means call function again and again
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print(fact(5))
            