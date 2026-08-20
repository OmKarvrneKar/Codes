from Basic import function
s=input("Enter the string: ")
print(len(s))

print(s[0])
print(s[-1])
    
#==============
n=input("enter the value")
m=[]
for i in n:
    if i in "AEIOUaeiou":
        m.append(i)
print(len(m))

#==================
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