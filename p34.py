# calculate the LCM of given numbers 
No1 = 12
No2 = 15

Max_no = No1 if No1>No2 else No2

while True:
    if Max_no % No1 ==0 and Max_no % No2 ==0:
        print("The LCM of two given number is : ",Max_no)
        break
    else:
        Max_no+=1
        