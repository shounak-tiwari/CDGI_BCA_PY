# if-elif-else : it is type of control statement which refers if the condition is true then terminate all rest condition and execute thier if not then check one by one if all are false return or execute else condition block... 


number = int(input("enter the number for check it is divided by 2,3, or 5 : "))

if number%2 == 0:
	print("The number is divide by two ")

elif number %3 ==0:
	print("The number is divide by three ")
elif number % 5 ==0:
	print("The number is divide by five ")
else:
	print("The number is not divided by two , three and five")