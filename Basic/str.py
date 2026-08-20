n=input("enter the value")

l=len(n)
for i in range(l):
    if n[i] in "aeiouAEIOU":
        q=n[i]
        print(len(q), end=" ")


