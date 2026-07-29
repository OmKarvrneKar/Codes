arr =  list(map(int , input().split()))
n=len(arr)

# for i in arr:

#     print(i)
#------------------------- print all elem

# sum=0
# for i in arr:
#     sum += i
# print(sum)
# ----------------print sum of arry


# n= max(arr)
#print(n)
val=[]

for i in range(n):
     sum=0
     for j in range(i,i+1):
        sum +=arr[j]
        val.append(sum)
     print(val)

 

    