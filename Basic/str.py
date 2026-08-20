n=input("Enter the string: ")
n.strip()
m=[]
q=[]
for i in n:
    if i in "AEIOUaeiou":
        m.append(i)
    else:
        q.append(i)
print("vowels",len(m))
print("consonants",len(q)) 