s1 = {1,2,3,4,5,6,7}
s2 = {1,3,6,7,8,9,10,11}

# Element of s1 and s2 area unique elements 
# 2,4,5,8,9,10,11 ( different element of s1 or s2 )

ans = s2.symmetric_difference(s1)
print(ans)
