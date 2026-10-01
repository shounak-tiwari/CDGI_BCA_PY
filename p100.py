# implementations is hide 
# share only neccessary details 
from abc import ABC,abstractmethod
class Area(ABC):
    @abstractmethod
    def __init__(self,l,b):
        self.l= l 
        self.b = b
    @abstractmethod
    def area(self):
        return self.l*self.b
class Ractangle(Area):
    def __init__(self,length,breadth):
        Area.__init__(self,length,breadth)
    def area(self):
        return Area.area(self)    

obj = Area(10,20)
print(obj.area())
