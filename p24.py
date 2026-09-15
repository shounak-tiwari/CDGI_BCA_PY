# code - write a program for check second largest number between three number 
x  = int(input("Enter the value of x "))
y  = int(input("Enter the value of y "))
z  = int(input("Enter the value of z "))

#for x is second largest 
if ((x>y and x<z) or (x>z and x<y)):
	print("X is second largest ")
elif ((y>x and y<z) or (y>z and y<x)):
	print("Y is second largest ")
else:
	print("Z is second largest ")