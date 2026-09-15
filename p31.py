#write a program for enter a number and print its second highst factor
num = int(input("Enter the number : "))
factor = 0 
i=1 

while i<num:
    if num%i==0:
        factor = i
    i+=1

print("The second highest factor is : ",factor)