# Abstractions : Abstraction is one of piller of object oriented programming.... which is use for hide the details of implementatin and show neccessary details only , in python abstraction is perform using abc module 


from abc import ABC,abstractmethod

# abstract class 
class Process(ABC):
    @abstractmethod
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    @abstractmethod
    def Area(self):
        return self.length*self.breadth
    
    @abstractmethod
    def perimeter(self):
        return 2*(self.length+self.breadth)

    