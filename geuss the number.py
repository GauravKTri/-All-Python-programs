
number_of_guesses=1
a=18
while(number_of_guesses<=5):
    num=int(input("Enter the number:\n"))
    if num>a:
        print("geuss lesser number:\n")
        
    elif num<a:
        print("geuss bigger number:\n")
        
    else:
        print("your answer is correct:\n")
        print("Game over")
        break
    print(5-number_of_guesses,"number of guesses left:\n")
    number_of_guesses=number_of_guesses+1
print("you took",number_of_guesses,"chances")
if (number_of_guesses>5):
    print("you loose")