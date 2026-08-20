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
#================
pal=input("enter the value")
if pal==pal[::-1]:
    print("palindrome")
else:
    print("not a palindrome")       
    #=======================
n=input("enther input")
cha=input("enter charecter")
m=[]
for i in n:
    if i in cha:
        m.append(i)
print(len(m))
#=================
n=input("enther input")
cha=input("enter charecter")
m=-1

for i , val in enumerate(n):
    if val == cha:
        m=i
        
print(m)   

