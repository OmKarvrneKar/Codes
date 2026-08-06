a,b=list(map(int,input().split()))
a,b=b,a
print(a,b)
# # swapping 2 no 


#3014
def minimumpushes(word):
    n= len(word)
    ans =0
    i=1
    while n>0:
        ans+=i*min(8,n)
        n-=8
        i+=1
    return ans




print(minimumpushes("helloworld"))

#3407

a,b=map(int,input().split())
a,b=b,a
print(a,b)

#1)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
collage=input("Enter your college name: ")

#2
x,y,z=map(int,input().split())#or x ,y, z=10,20,30

#3
a,b,c=50,50,50
print(a,b,c)    

#4
a,b=30,15
a,b=b,a                        
print(a,b)                     


#5
q=13
w=15.0
r="raj"
t=True
print(type(q))
print(type(w))  
print(type(r))
print(type(t))  

#6
a,b=map(int,input().split()) 
a,b=b,a                       
print(a,b)                     

#7
std={"student":"rahul","marks":92}
print(std)  

#8
x=10
y=x
x=20
print(x,y)


# typecasting
a="20"
print(a)
b=int(a)
print(type(b))
print()

#1
a=1
print(type(a))

#2
age=input("Enter your age: ")
print(type(age))
print(int(age))

a = "10"
b = 20

print(a + str(b))

a = int("25")
b = float("10")

print(a + b)
print(type(a + b))

#53 maximum subarray sum
nums = [-2,1,-3,4,-1,2,1,-5,4]

res=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        res.append(nums[i:j])

sub_arry = max(sum(sub_lst) for sub_lst in res)
print(sub_arry)



#-=========
arr=[1,2,3,4,5]
arr.pop()
print(arr)

#=================

a = int(input("enter the val: "))
if a%2==0:
    print("Even")
else:
    print("Odd")

#=============
o,t=map(int, input().split())

if o>t:

    print("one is larger ")
else:
    print("two is larger")

#=========================

l,a,r=map(int,input().split())

if (l>a and l>r):
    print("l is larger")
elif (a>l and a>r):
    print("ais larger")
else: print("r is larger")

#================
year=int(input("Enter a year: "))
if (year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")
#========================

radius=int(input("Enter the radius of the circle: "))
pi=3.14
area=pi*radius**2
print("Area of the circle is: ",area)

#========================

celsius=int(input("Enter the temperature in Celsius: "))
fahrenhit=(celsius*9/5)+32
print("Temperature in Fahrenheit is: ",fahrenhit)
#======================
a=1
b=2
a,b=b,a
print(a,b)

#=========================
a,b,c=map(int,input().split())
if a<b and a<c:
    print("a is smaller")
elif b<a and b<c:
    print("b is smaller")
else:
    print("c is smaller")
#=========================

m=-10
if m>0:
    print("positive")
else: print("negative")
#=========================
marks=int(input("enter the marks"))
if marks>=90:
    print("A")
elif marks>=80 and marks<90:
    print("B")
elif marks>=70 and marks<80:
    print("C")  
elif marks>=60 and marks<70:
    print("D")
else :
    print("F")
#======================
char1= input("enter the letter")
if char1.isupper():
    print("uppercase")
else:
    print("lowercase") 
#=========================
s1=int(input("entet the ine side :"))
s2=int(input("entet the ine side :"))
s3=int(input("entet the ine side :"))
if s1+s2>s3 or s1+s3>s2 or s2+s3>s1:
    print("its triangle")
else:
    print("not a triangle")


#+=========================
n=int(input("enter the number"))

if n%3==0 and n%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3 and 5")
#=========================

a=int(input("enter the first angle: "))
b=int(input("enter the second angle: "))
c=int(input("enter the third angle: "))
triangle_sum = a + b + c
if triangle_sum == 180:
    print("The angles form a valid triangle.")
else:
    print("The angles do not form a valid triangle.")
#=========================
input_no=int(input("enter the number: "))
if input_no%100==0 :
    print("year is century year")
else:
    print("year is not century year")   
#=========================
n = 12345

print(len(str(n)))