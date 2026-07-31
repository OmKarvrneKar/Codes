class employee:
    def __init__(self, name, salary):
        self.__name = name # PRIVATE attribute (__)===> USED TO MAKE ATTRIBUTE PRIVATE
        self.__salary = salary 

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            raise ValueError("Salary must be a positive value.")