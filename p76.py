cbcNormal = {
    "Hemoglobin":[(13.0,17.5), (12.0,16.0)],
    "rbc":[(4.3,5.9),(3.5,5.5)],
}

# print normal lowest range of women 
print(cbcNormal["Hemoglobin"][1][0])
print(cbcNormal["Hemoglobin"][1][1])

# print lowest range of rbc in women
print(cbcNormal["rbc"][1][0])
print(cbcNormal["rbc"][1][1])

# lowst rbc range of men 
print(cbcNormal["rbc"][0][0])