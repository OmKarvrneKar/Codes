def add(a,b):
    return a+b

print(add(10,20))
#====================
def is_even(n):

    if n%2==0:
        return True
    else:
        return False

print(is_even(10))
#==================
def maximun(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(maximun(10,20,30))
#==================
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact 

print(factorial(5))
#================== 
def reverse(n):
    rev=0
    while n>0:
        rev=(rev*10)+(n%10)
        n//=10
    return rev

print(reverse(12345))