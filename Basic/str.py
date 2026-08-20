n=input("enter the value")
count=0
l=len(n)
for i in range(l):
    if n[i] in "aeiouAEIOU":
        count=n[i]+1
    print(count, end=" ")

