# private protected memebers in pythons 
class Introduction:
    def __init__(self,name,age,contact):
        self.name = name # public attribute
        self._age = age # protected self and child 
        self.__contact = contact #private not sharing 

object1 = Introduction("Akash",26,8718828288)
# print(object1.name)
# print(object1._age)
object1.__contact = 8718828288
print(object1.__contact)