try:
    a= int(input("enter a number : "))
    b= int(input("enter a number : "))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("division by zero is not possible")   
except ValueError:
    print("invalid input") 
#======================================================
try:
    num=int(input("enter a number : "))
    print(num)  
except ValueError:
    print("invalid input")  

# #====================================================  
try: 
    aa=int(input("enter a number : "))
    bb=int(input("enter a number : "))
    cc=aa/bb
    print(cc)
except (ZeroDivisionError, ValueError):
    print("invalid input or division by zero") 
# #====================================================

try :
    a= int(input("enter a number : "))
    b= int(input("enter a number : "))
    c=a/b
    
except ZeroDivisionError:
    print("division by zero is not possible")
else: 
    print(c)



# try: 
#     file=open("DEMO","r")
#     print(file.read())

# except FileNotFoundError:
#     print("file not found")

# finally:
#     print("program finished")

# no=[10,20,30,40,50]
# try:
#     print(no[10])
# except IndexError:
#     print("out of range")

# stud={"name":"omkar","age":20,"rollno":101}
# try:
#     print(stud["marks"])
# except KeyError:
#     print("key not found")



# corre_pass= "password123"
# try: 
#     password=input("enter password : ")
#     if password != corre_pass:
#         raise ValueError("invalid password")
#     print("login successful")
# except ValueError as e:
#     print(e)

balance=1000
try:
    amout=int(input("enter amount to withdraw : "))
    if amout>balance:
        raise ValueError("insufficient balance")
    balance -=amout

    print("withdrawal successful",balance)
except ValueError as e:
    print(e)   

try:
    marks=int(input("enter marks : "))
    if marks<0 or marks>100:
        raise ValueError("invalid marks")
    print("valid marks")
except ValueError as e:
    print(e)

try:
    a =int(input("enter a number : "))

    try:
        b=int(input("enter a number : "))
        print(a/b)
    except ZeroDivisionError:

        print("division by zero is not possible")

except ValueError:
    print("invalid input")  


try:
    a=int(input())
    b=int(input())

    print(a/b)

except (ValueError,ZeroDivisionError) as e:
    print(e)

