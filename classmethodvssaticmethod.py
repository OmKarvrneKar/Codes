# Define a simple student class
class student:
    name ="virat loli"
    age = 35

# Create an instance of student and access class attributes
s=student()
print(s.name)   
print(s.age)        

# Define another class std
class std:
    def display(self):
        # A simple instance method
        print("this is an student classs")

# Create an instance of std and call display
s=std()
s.display()

#==================================

class student:
    college="abc college" # Class attribute

    def __init__(self, name,age):
        # Initialize instance attributes
        self.name=name
        self.age=age
        

s1 = student("omkar", 20)
# print(s1.name)
# print(s1.age)
print(s1.college)   

#===============================
@classmethod
def changeCollage(cls , newcollage):
    cls.college=newcollage
@staticmethod
def greet():
    print("hello welcome to student class")

s= student("omkar", 20)
print(student.college)

student.changeCollage("IISC")

print(student.college)
student.greet()


