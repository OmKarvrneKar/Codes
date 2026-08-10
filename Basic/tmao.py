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