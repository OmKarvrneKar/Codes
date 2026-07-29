arr = list(map(int, input().split()))   
# map(function, iterable) applies the function to each item of the iterable (like a list) and returns a map object. In this case, it converts each input string to an integer and creates a list of integers.
k=int(input())
n=len(arr)
sum_arry=[]

for i in range(n-k+1):
    sum = 0
    for j in range(i, i+k):
        sum += arr[j]
        
    sum_arry.append(sum)

print(sum_arry)