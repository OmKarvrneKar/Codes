# def largest(n):
#     max_dig=0
#     while n>0:
#         digi=n%10
#         if digi>max_dig:
#             max_dig=digi
#         n//=10
#     return max_dig
        
# m=12345
# print("Largest digit in the number is: 12345 ",largest(m))

#==========================
# def count_of_perticular(n,d):
#     count=0
#     while n>0:
#         if  n%10==d:
#             count+=1
#         n//=10
#     return count
# m=123455
# d=5
# print(count_of_perticular(m,d))
#==========================


# def remove_zero(n):
#     result=0
#     while n>0:
#         remove=n%10
#         if remove!=0:
#             result=(result*10)+remove
#         n//=10
#     return reverse(result)
    

# def reverse(n):
#     rev=0
#     while n>0:
#         rev=(rev*10)+n%10
#         n//=10
#     return rev


# m=123450
# print("Number after removing zeros is: 123450 ",remove_zero(m))



#amstri=ong number Armstrong Number ⭐⭐⭐


#Now retry the Armstrong problem you previously got wrong.

#Input: 153 Output: Armstrong
def is_armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    return sum==n

m=153
if is_armstrong(m):
    print("The number is Armstrong")    
else:
    print("The number is not Armstrong")