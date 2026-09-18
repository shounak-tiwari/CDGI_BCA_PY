for i in range(97,102):
    for spc in range(1,102-i):
        print("_",end=" ")
    for j in range(97,i+1):
        print(chr(j),end=" ")
    print("")