# complete blood count calculator.......
normalRange= {
    "Hemoglobin":[13.0,17.5],
    "RBC":(4.3,5.9),
    "Hematocrit" : (41,53)
}
hb = float(input("Enter the range : "))  #26 
lowrange  = normalRange['Hemoglobin'][0] 
highrange = normalRange['Hemoglobin'][1]
if hb>=lowrange:
    if hb<=highrange:
        print("its in normal")
    else:
        print("its high from normal range")
else:
    print("its low from normal rnage")