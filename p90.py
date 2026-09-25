lst = [1,2,3,4,5,6,7,8,9]
def medianValue(lst:list):
    # step 1 : sort the list 
    lst.sort()
    if len(lst)%2==0:
        midx = len(lst)//2 -1
        return lst[midx]
    else:
        midx = len(lst)//2
        return lst[midx]

result = medianValue(lst)

print(result)