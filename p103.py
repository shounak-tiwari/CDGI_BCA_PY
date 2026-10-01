# import class process from program number 101 
from p101 import Process
class Ractangle(Process):
    def __init__(self, length, breadth):
        super().__init__(length, breadth)
    
    def Area(self):
        return super().Area()
    
    def perimeter(self):
        return super().perimeter()
    

# object of Ractangle class  
obj1 = Ractangle(10,20)
print(obj1.perimeter())