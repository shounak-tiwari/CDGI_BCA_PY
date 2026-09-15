# write a program to print and calculate the factors of numbers 
num=20
i=1
factor =0 
while i<=num:
    if num%i==0:
        factor+=1
    i+=1
if factor ==2:
    print("Number is prime ")
else:
    print("Number is not prime")