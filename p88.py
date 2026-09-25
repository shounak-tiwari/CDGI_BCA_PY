from p87 import average_mean

employee_details ={
    "name":["x","y","z"],
    "salary":[1000,10000,100000]
}

average_salary = average_mean(employee_details["salary"])
print(average_salary)