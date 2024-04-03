from random import randint

# we need to make a variable to hold "rock, paper, scissors". We also need to have the computer pick one of the moves,
# so we will use randint to pick a random move from our rps list. We also need to start the game so we set game to
# True so that the game will run
rps = ["Rock", "Paper", "Scissors"]
game = True

# here we make a loop set to true so that the coop continues forever
while game == True:
    computer = rps[randint(0,2)]
    # now we need to get the users move of "rock, paper, scissors"
    playerinput = input("Rock, Paper, Scissors? ")
    
    # we need to check if the user and computer tied
    if playerinput.lower() == computer.lower():
        print("Tie!")
    
    # so if the user picked rock    
    elif playerinput.lower() == "rock":
        # and if the computer picked paper, then we tell the user that they lose and that paper covers rock
        if computer == "Paper":
            print("You lose!", computer, "covers", playerinput)
        # the last choice that the computer could have picked is scissors because we checked for a tie then we tell the
        # user that they won
        else:
            print("You win!", playerinput, "smashes", computer)
            
    # now we need todo that same thing but for the rest of the options, so paper and scissors
    elif playerinput.lower() == "paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", playerinput)
        else:
            print("You win!", playerinput, "covers", computer)
            
    elif playerinput.lower() == "scissors":
        if computer == "Rock":
            print("You lose...", computer, "smashes", playerinput)
        else:
            print("You win!", playerinput, "cut", computer)
            
    # if for whatever reason the code didnt run any of the options then we will print out this
    else:
        print("Try again, Check your spelling!")

    # lastly to make sure that the code keeps runing we will set the game to True and we need to redo the ranint function
    # so that the computer picks a different move
    game = True