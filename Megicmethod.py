class student:
    """A simple student class to demonstrate magic methods."""
    def __init__(self, marks):
        # Initialize the private marks attribute
        self.__marks = marks  # magic method __init__ is used to initialize the object with marks

    def __str__(self):
        # Return a string representation of the object
        return f"Student marks: {self.__marks}"

    def __add__(self, other):
        # Allow addition of two student objects based on their marks
        return self.__marks + other.__marks

# Create two student instances
s1 = student(85)
s2 = student(90)

# Print string representation
print(s1)  # Output: Student marks: 85
# Print addition of two student objects
print(s1 + s2)  # Output: 175