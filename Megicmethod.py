class student:
    def __init__(self, marks):
        self.__marks = marks  # magic method __init__ is used to initialize the object with marks

    def __str__(self):
        return f"Student marks: {self.__marks}"

    def __add__(self, other):
        return self.__marks + other.__marks

s1 = student(85)
s2 = student(90)

print(s1)  # Output: Student marks: 85
print(s1 + s2)  # Output: 175