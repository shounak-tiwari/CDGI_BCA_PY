class RegisterEmployee:
    # self: it is tract your current object 
    def inputDetails(self):
        self.name = input("Enter the name of employee : ")
        self.age = int(input("Enter the age of employee : "))
        self.salary = int(input("Enter the Salary of employee : "))
    def printOutput(self):
        print("name of employee : ",self.name)
        print("age of employee : ",self.age)
        print("salary of employee : ",self.salary)
# Object of Employee 
objEmp = RegisterEmployee()
objEmp.inputDetails()
objEmp.printOutput()