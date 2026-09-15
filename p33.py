# write a program for calculate the lcm of two number 
# lowest common multiple 

# Write a program for calculate the hcf of two number 

no1 = int(input("Enter the number 1 : "))
no2 = int(input("Enter the number 2 : "))
min = no1 if no1<no2 else no2
while True:
    if no1 % min ==0  and no2 %min==0:
        print("HCF is : ",min)
        break
    else:
        min-=1