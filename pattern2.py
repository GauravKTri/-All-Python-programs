n=int(input("Enter number of rows:\n"))
b=int(input("enter 1 or 0:\n"))
if b is 1:
    count=0
    while(count<=n):
        print("*"*count)
        count=count+1
elif b is 0:
    count=n
    while(count!=0):
        print("*"*count)
        count=count-1