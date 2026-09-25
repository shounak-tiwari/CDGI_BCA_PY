def removeDuplicateData(data):
    data = {
        "name" : data["name"][::-1],
        "income": data["income"][::-1]
    }
    for x in data["name"]:
        if data["name"].count(x)==2:
            data["income"].pop(data["name"].index(x))
            data["name"].remove(x)

    data = {
        "name" : data["name"][::-1],
        "income": data["income"][::-1]
    }
    print(data)
        
