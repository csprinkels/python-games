# this line let’s us take any variable (a item/object) and have
# the computer randomly pick that item
from random import randint

# here we made a variable ht that stores our words “Heads or Tails”
ht = ["Heads", "Tails"]

# we made a variable called game which we set to false so that we can create a loop
# that lets us play Heads or Tails as long as we want
game = True

# here we start our loop that lets us play the game
while game == True:
    coinflip = ht[randint(0,1)]
    
    # this input line lets the player type in weather they want to choose heads or tails
    # and stores their answer
    playerinput = input("Heads or Tails? ")
    
    # in this loop if the player types in heads, it’ll match the text weather they typed
    # capital or lowercase
    if coinflip == "Heads":
        # now that we have they players input we need to see what the coin landed on,
        # so with that if the coin landed on tails then you lose
        if playerinput.lower() == "tails":
            print("It was Heads, you lose")

        # or else then it landed on heads then you won    
        elif playerinput.lower() == "heads":
            print("It was Heads, you win")


    # here we do the same thing but for tails 
    elif coinflip == "Tails":
        if playerinput.lower() == "heads":
            print("It was Tails, you lose")
            
        elif playerinput.lower() == "tails":
            print("It was Tails, you win")

    # if you’re like me and can’t spell sometimes the this 
    # will print out telling you to try again        
    else:
        print("Check your spelling")
        
    coinflip = ht[randint(0,1)]
    game = True