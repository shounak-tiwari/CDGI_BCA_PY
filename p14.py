#Vijay Take loan from HDFC bank of K principle, R rate and T time , all needed input is #enter through the user input print simple interest and total amount paid by vijay.. 

K = float(input("Enter the principle amount  : "))
R = float(input("Enter the rate of interest : "))
T = int(input("Enter the time in year  : "))

Simple_interest  = (K*R*T)/100
Amount  = Simple_interest + K

print("The loan amount is : ", K)
print("The interest is : " , Simple_interest)
print("The Amount is : ", Amount) 