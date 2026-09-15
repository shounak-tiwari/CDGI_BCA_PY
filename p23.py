year = int(input("Enter the year : "))

if year % 4 == 0 and year %100!=0:
	print("year is leap ") 
elif year %400==0:
	print("year is leap")
else:
	print("year is not a leap ")