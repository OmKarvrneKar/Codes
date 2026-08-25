# for i in range(1,11):
#     print(i)

# # #=========================
# for j in range(10,0,-1):
#     print(j)
# # #=========================
# for k in range(2,21,2):
#     print(k)
# # #=========================
# for l in range(1,20,2):
#     print(l)
# #=========================S
# for m in range(7,71,7):
#     print(m)
# #==========================

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

# #========================

# sum=0
# for i in range(2,101,2):
#     sum+=i
# print(sum)
# #========================
# Input=int(input(" "))
# fact=1
# for i in range(1,Input+1):
#     fact*=i
# print(fact)
# #====================
# for  i in range(50,101):
#     print(i)
# #=========================
# for  i in range(1,6):
#     print("*" * i)

#==========================
n=12345
print("Reverse of the number is: 12345 ",str(n)[::-1])
# #========================
n=987654
print("count of digits in the number is: 987654 ",len(str(n)))
# #========================
n=12345
sum=0
for i in str(n):
    sum+=int(i)
print("sum of digits in the number is: 12345 ",sum)
# #========================
n=121
if str(n)==str(n)[::-1]:
    print("The number is palindrome")
else:
    print("The number is not palindrome")
# #========================
n=153
sum=0
for i in str(n):
    sum+=int(i)**len(str(n))
    if sum==n:
        print("The number is armstrong" )
    else:
        print("The number is not armstrong")

#=========================
n=18
for i in range(2,n):
    if n%i==0:
        print("The number is not prime")
        break
    else:
        print("The number is prime")
        break
#=========================
def fubo(n):
    a,b=0,1
    result=[]
    for i in range(n):
        result.append(a)
        a,b=b,a+b
    return result
print(fubo(10))

#=========================
# reverse of a number
def reverse(n):
    rev=0
    while n>0:
        rev=(rev*10)+n%10
        n//=10 
    return rev

m=12345
print("Reverse of the number is: 12345 ",reverse(m))
#=========================
def count(n):
    count=0
    while n>0:
        count+=1
        n//=10
    return count

m=12345
print("Count of digits in the number is: 12345 ",count(m))
#=========================
def sum(n):
    sum=0
    while n>0:
        sum+=n%10
        n//=10
    return sum

m=12345
print("Sum of digits in the number is: 12345 ",sum(m))
#=========================
def reve(n):
    temp=0
    while n>0:
        temp=(temp*10)+n%10
        n//=10
    return temp

if reve(m)==m:
    print("The number is palindrome")
else:
    print("The number is not palindrome")

m=153
print("Reverse of the number is: 153 ",reve(m))
#==================
# prodeuct
def pro(n):
    prod=1
    while n>0:
        prod*=n%10
        n//=10
    return prod     

m=12345
print("Product of digits in the number is: 12345 ",pro(m))
#=========================
def largest(n):
    max_dig=0
    while n>0:
        digi=n%10
        if digi>max_dig:
            max_dig=digi
        n//=10
    return max_dig
        
m=12345
print("Largest digit in the number is: 12345 ",largest(m))
#=========================
def count_of_perticular(n,d):
    count=0
    while n>0:
        if  n%10==d:
            count+=1
        n//=10
    return count
m=123455
d=5
print(count_of_perticular(m,d))

#==========================
def remove_zero(n):
    result=0
    while n>0:
        remove=n%10
        if remove!=0:
            result=(result*10)+remove
        n//=10
    return result

m=123450
print("Number after removing zeros is: 123450 ",remove_zero(m))
#==========================