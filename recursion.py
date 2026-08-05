#Fibonacci series using recursion
def fibo(n):
    a,b=0,1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result

n=int(input(" "))
print(fibo(n))



# factorial of a number using recursion
def factorial(n):
    if n==0 or n==1: #checking if n is 0 or 1, as the factorial of both is 1
        return 1 #return 1 if n is 0 or 1
    else:
        return n*factorial(n-1) #recursively calling the factorial function with n-1 until it reaches the base case (n=0 or n=1)
n=int(input(" "))
print(factorial(n))

