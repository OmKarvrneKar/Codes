file = open("student.txt","w")

file.write("hello " )
file.write("this is omkar")

file.close()

print("data written successfully")
#===============
file = open("student.txt","r")

data =file.read()
print(data)

file.close()
#=======================

file=open("student.txt","r")
print(file.readline())

file.close()
#============

source = open("student.txt","r")
distination = open("copy_student.txt","w")

distination.write(source.read())

source.close()
distination.close() 

print("file copied successfully ") 

#==========================
file = open("student.txt","r")

data =file.read()

upper =0
lower =0
for i in data:
    if i.isupper():
        upper +=1
    elif i.islower(): 
        lower +=1

print("number of uppercase letters : ",upper)
print("number of lowercase letters : ",lower)  



