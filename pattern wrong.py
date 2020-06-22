print("pattern printing")
a=int(input("Enter how many rows you want:\n"))
print("Enter 1 or 0")
b=bool(input("1 for true and 0 for false:\n"))
if b=="1":
    for i in range(0,a+1):
        print("*"*i)
if b=="0":
    for i in range(a,0,-1):
        print("*"*i)