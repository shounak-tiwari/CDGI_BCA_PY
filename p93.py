class Employee:
    def __init__(self):
        print("Hey ! i'm constructor call automatically when object has created ")
        self.name = input("enter the name  : ")

E1 = Employee()
print(E1.name)