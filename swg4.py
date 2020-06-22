import random
print("Welcome to snake water gun game....Enjoy!")
print("remember you have only 10 chances")
i = 0
chances = 10
machine = 0
player = 0
draws = 0
while(i<10):
    choices = ["snake", "water", "gun"]
    computer = random.choice(choices)
    user = input("Enter your choice: snake, water, gun \n")
    if (computer=="snake" and user=="snake")or(computer=="water" and user=="water")or(computer=="gun" and user=="gun"):
        draws = draws + 1
        chances = chances - 1
        print(f"It's a tie \n chances left:{chances}\n scores so far:\nmachine:{machine}\nplayer:{player}\ndraws:{draws} ")
    elif (computer=="snake"and user=="water")or(computer=="gun"and user=="snake")or(computer=="water"and user=="gun"):
        machine = machine + 1
        chances = chances - 1
        print(f"computer wins \n chances left:{chances}\n scores so far:\nmachine:{machine}\nplayer:{player}\ndraws:{draws} ")
    elif (computer=="snake"and user=="gun")or(computer=="gun"and user=="water")or(computer=="water"and user=="snake"):
        player = player + 1
        chances = chances - 1
        print(f"you win \n chances left:{chances}\n scores so far:\nmachine:{machine}\nplayer:{player}\ndraws:{draws} ")

    else:
        print("sorry wrong input cannot be processed")
        break
    i = i + 1
if chances==0 and player>machine:
    print(f"Congratulations you won the game\n Final scores are:=\n machine = {machine}\n player = {player} ")
elif player==machine:
    print("WOW Its a Tie , be confident you'll win next time")
else:
    print("Better luck next time You loose the game!")


