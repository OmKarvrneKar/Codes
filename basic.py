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