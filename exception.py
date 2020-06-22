print("Enter num 1")
a=input()
print("Enter num 2")
b=input()
try:
    print("The sum is",
    int(a)+int(b))
except Exception as e:
    print(e)