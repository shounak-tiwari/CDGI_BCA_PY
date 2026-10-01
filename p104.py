# Inheritance : it is one of major important piller of object oriented programming its means is reuse the properities of base or parent class into child class the meaning of interit is reuse , and  those class have no parent class and share the properities with the another class called parent class and those class have a parent and it use the properties of another class and share thier properies to another class classed intermidate class and those class only use the properites of another class and not share its properies to any one called child class... its another name is derived class also... 

# class which store the data of personal details 
class PersonalDetails:
    def __init__(self,name,contact, dob,address):
        self.name = name
        self.contact = contact
        self.address = address
    def getDetails(self):
        return f"The name of employee {self.name} , contact  : {self.contact} and address : {self.address}"
    
# class which store the data of acedemic details
class AcademicDetails:
    def __init__(self,**kwargs):
        self.academicdict = kwargs
    def getDetails(self):
        return self.academicdict 
    
class EmployeeClass(AcademicDetails,PersonalDetails):
    def __init__(self,name ,contact,dob,address,**kwargs,):
        AcademicDetails.__init__(self,**kwargs)
        PersonalDetails.__init__(self,name,contact,dob,address)
    def getDetails(self):
        return AcademicDetails.getDetails(self), PersonalDetails.getDetails(self)
    


# object of employee class 
objEmp = EmployeeClass("Akash",8718828288,'00-00-2000','indore',high = "ms",highersec="ms")

print(objEmp.getDetails())
    