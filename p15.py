#A teacher has a certain number of chocolates and wants to distribute them equally among #the students in her class. Take the total number of chocolates and the number of #students as input from the user. Print how many chocolates each student gets, and how # many chocolates are left over.


no_of_Student  = int(input("Enter the number of student : " ))
no_of_chocolates = int(input("Enter the number of chocolates : "))

perstudent = no_of_chocolates // no_of_Student 

remain = no_of_chocolates % no_of_Student 

print(perstudent)
print(remain)