# def counte(n):
#     count=0
#     while n>0:
#         if n%2==0:
#             count+=1
#         n//=10  
#     return count
# m=123456
# print(counte(m))
# #==========================

def count_odd(n):
    count=0
    while n>0:
        if n%2!=0:
            count+=1
        n//=10
    return count
m=12346
print(count_odd(m))
