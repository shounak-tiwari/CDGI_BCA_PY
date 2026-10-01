import pickle 
import uuid
FILE = open("student.pkl","wb")
class StudDetails:
    def __init__(self):
        self.object_id = uuid.uuid4()
        self.name  = input("Enter the name : ")
        self.address = input("Enter the address : ")
        self.contact = input("Enter the contact  : ")
    # Create files 
    def dataSave(self):
        data = {
            self.object_id : {"name":self.name,"address":self.address}
        }
        pickle.dump(data,FILE)
        print("data is saved ")

obj1 = StudDetails()
obj1.dataSave()
print(obj1.object_id)