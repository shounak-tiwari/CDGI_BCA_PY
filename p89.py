# write a program where enter a data in dict form print the mode of the data using custom functions 
def mode(lst:list):
    mode_value = 0
    count_value = 0
    for x in lst:
        if lst.count(x) >count_value:
            mode_value = x 
            count_value = lst.count(x)    
    print(mode_value)

lst = [8,2,3,4,5,6,1,1,1,1,6,3,4,4,4,4,4,4,4,4,4,5,]
mode(lst)