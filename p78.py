# ordered , mutable
d1 = {
    "first_name":"Akash",
    "last_name":"Tiwari",
    "role":"mlengi",
    "company":"ypsilon it solutions",
    "city":"indore",
    "pincode":452010
}

# add new item into a dict 
d1.setdefault("employeeId","Uni02FEB2023-136")

# iterate the items of dict using for loops 
for k,v in d1.items():
    print(f"{k} : {v}")