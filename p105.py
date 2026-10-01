# create a base class whose name is vechile it have two properites milage and price create two child car and bike inherit vechile and demonstraction of insertion and getting 
# base class  
class Vechile:
    def __init__(self,milege,price):
        self.milage = milege
        self.price = price
    
    def getDetails(self):
        return f"The milage of vechile is {self.milage} and price is {self.price}"
# bike is inherit from vechile class : bike is derieved class and vechile is base class 
class Bike(Vechile):
    def __init__(self, milege, price):
        super().__init__(milege, price)
    def getDetails(self):
        return super().getDetails()

bikeObj = Bike("70km/l",112000)
print(bikeObj.getDetails())