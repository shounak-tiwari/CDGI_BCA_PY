_2ndyears = {'Ajay','Vijay','Sunder','Susheel','Lalit','RajPal','Rakesh','Kunal'}

_fail = {'Susheel','Lalit','RajPal'}

_3rdyears = {'Ajay','Vijay','Sunder','Susheel','Lalit','RajPal','Rakesh','Kunal','Vinod','Sarpanchji','Prahlad','Abhishek','Vanrakash','Vidhayak'}


# print the name of students who is transfers 

transfer  = _3rdyears.difference(_2ndyears)
print(transfer)
