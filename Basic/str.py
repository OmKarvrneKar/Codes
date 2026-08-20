n=input("enter the value")

l=len(n)
for i in range(l):
    if n[i] in "aeiouAEIOU":
        q=len(n[i])

        print(q, end=" ")


