# import openpyxl beacuse it is responsible for read write manipulation and operations on excel files or work book 
import pandas as pd
wb = pd.read_excel(r"C:\Users\Akash\OneDrive\Desktop\CDGI-A1\Students_Result_Analysis.xlsx")
for element in wb['Student_ID']:
    print(element)