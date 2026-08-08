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
