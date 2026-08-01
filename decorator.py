def decorrator(func):

    def wrapper():
        print("before function")
        func()
        print("after function")

    return wrapper

@decorrator
def greet():
    print("helllo")

greet() 

# decorator is a function which takes another function as an argument and extends the behavior of this function without explicitly modifying it.