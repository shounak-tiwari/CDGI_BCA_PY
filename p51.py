for i in range(1,6):
    for spc in range(1,6-i):
        print(" ",end="")
    
    for star in range(1,i+1):
        print("*",end="")
    print("")