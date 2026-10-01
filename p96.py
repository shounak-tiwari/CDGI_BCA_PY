import pickle 

file = open("student.pkl","rb") 
data = pickle.load(file)
print(data)