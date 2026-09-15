#write a program for print 1 to n odd numbers... 

i = 1
n = int(input("Enter the nth term : "))

while i<=n:
    if i%2!=0:
        print(i,"is even number")
    i+=1