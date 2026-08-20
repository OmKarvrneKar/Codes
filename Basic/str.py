n=input("enther input")
cha=input("enter charecter")
m=[]
for i in n:
    if i in cha:
        m.append(i)
print(len(m))
