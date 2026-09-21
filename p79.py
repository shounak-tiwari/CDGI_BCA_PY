d1 = {
    "first_name":"Akash",
    "last_name":"Tiwari",
    "city":"indore",
    "pincode":452010
}
d2 = {
    "role":"mlengi",
    "company":"ypsilon it solutions",
    "project":"US_34512007658_IDMLOOPS"
}
d1.update(d2)

# print(d1)
# print(d1.keys())
# print(d1.values())
# print(d1.items())
# add an items into a dict setdefault 
# remove an item from the last of dict 
# d1.popitem()
# print(d1)
# remove an item from the dict 
# d1.pop("pincode")
# print(d1)

print(d1.get("first_name"))