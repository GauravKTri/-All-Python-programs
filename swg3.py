import random

print("Let\'s start the game \"Snake Water Gun\"")
count = 0
win = 0
draw = 0
lst = ["Snake", "Water", "Gun"]#maaf karo yaar, bina list ka kuch sujta nahi hai
print("0-Snake, 1-Water, 2- Gun")
while count<10:
    cpu = random.randint(0,2)
    print("********TURN - ", str(count+1), "********")
    you = int(input("Please insert your choice : "))
    while you>2 or you<0:
        print("Your input is not valid")
        you = int(input("Please insert again : "))
    print("Your Choice : ", lst[you])
    print("Computer's Choice : ", lst[cpu])
    if you == cpu:
        print("Draw")
        draw += 1
    else:
        if you == 0:
            if cpu == 1:
                print("You win the Game")
                win += 1
            if cpu == 2:
                print("You lost the Game")
        elif you == 1:
            if cpu == 0:
                print("You lost the Game")
            if cpu == 2:
                print("You win the Game")
                win += 1
        elif you == 2:
            if cpu == 0:
                print("You win the Game")
                win += 1
            if cpu == 1:
                print("You lost the Game")
    count+=1
print("**************RESULTS**************")
print("You Win : ", str(win))
print("Computer Win : ", str(10-win-draw))
print("No. of Drawn : ", str(draw))