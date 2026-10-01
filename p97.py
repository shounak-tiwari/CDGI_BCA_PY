import pickle
import uuid
# distructor 
FILE = "record.pkl"
class Employee:
    def __init__(self,name,age,contact):
        self.name = name
        self.age = age
        self.contact = contact
    def saveToFile(self):
        data = {
            "name":self.name,
            "age":self.age,
            "contact":self.contact,
        }
        with open(FILE,"wb") as fp:
            pickle.dump(data,fp)
            print("data is saved into file")
    def __del__(self):
        print("delete all the memory automatically")
        
        
    
obj1 = Employee("akash",26,8718828288)
obj1.saveToFile()

obj2 = Employee("akash",26,8718828288)
obj2.saveToFile()

obj3 = Employee("akash",26,8718828288)
obj3.saveToFile()
