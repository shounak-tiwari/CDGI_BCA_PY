# Encapsulations : is piller of object oriented programming which is wrapped the member or member function into single unit ....  
class Employee:
    def __init__(self):
        self.__salary = None
    def setter(self,sal):
        self.__salary = sal
    def getter(self):
        return self.__salary
obj = Employee()
obj.setter(100)
print(obj.getter())