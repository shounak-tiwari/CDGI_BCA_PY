# nested if control statement : multiple conditions for single result ...

Per10 = float(input("Enter the percentage in high school examinations : "))
Per12 = float(input("Enter the percentage in higher sec. school examinations : "))
if Per10>55.00:
	if Per12>55.00:
		passout_year = int(input("Enter passout year e.g. 2025 "))
		if passout_year == 2025:
			pg = str(input("press y if your mca is completed : "))
			if pg=='y':
				print("eligible for screening test ")

