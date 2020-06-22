a=["ar","br",2,3,4,5,6,7,9,10,"asd"]
for item in a:
    if str(item).isnumeric() and item>6:
        print(item)