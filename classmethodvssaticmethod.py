class student:
    name ="virat loli"
    age = 35

s=student()
print(s.name)   
print(s.age)        



class std:
    def display(self):
        print("this is an student classs")

s=std()
s.display()

#==================================

class student:
    college="abc college"

    def __init__(self, name,age):
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


