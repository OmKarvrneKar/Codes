class duck:
    def walk(self):
        print("duck can walk")

class Human:
    def walk(self):
        print("human can walk")


def display(obj):
    obj.walk()

display(duck())  
display(Human()) 

# duck typing is feature of python where the type of object doesnot matter , what matter is  wehtetr the object has the required method or behavior or not. 
# In this example both duck and human have walk method so we can pass both objects to display function.
