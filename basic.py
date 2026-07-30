# a,b=list(map(int,input().split()))
# a,b=b,a
# print(a,b)
# # swapping 2 no 


#3014
def minimumpushes(word):
    n= len(word)
    ans =0
    i=1
    while n>0:
        ans+=i*min(8,n)
        n-=8
        i+=1
    return ans


print(minimumpushes("helloworld"))