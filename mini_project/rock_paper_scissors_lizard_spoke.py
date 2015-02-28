# Rock-paper-scissors-lizard-Spock (RPSLS) is a variant of Rock-paper-scissors that allows five choices. 
# Each choice wins against two other choices, loses against two other choices and ties against itself. 
# Much of RPSLS's popularity is that it has been featured in 3 episodes of the TV series "The Big Bang Theory". 

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:

# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

def name_to_number(name):
    # convert name to number using if/elif/else
    if name == "rock":
        return int(0)
    elif name == "Spock":
        return int(1);
    elif name == "paper":
        return int(2)
    elif name == "lizard":
        return int(3)
    elif name == "scissors":
        return int(4)
    else:
        return "Please enter correct string!"


def number_to_name(number):
    
    # convert number to a name using if/elif/else
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        return "Please enter an integer between 0 and 4!"


def rpsls(player_choice): 

    # print a blank line to separate consecutive games
    print ""
        
    # print out the message for the player's choice
    print "Player chooses " + player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0, 5)    
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)    
    
    # print out the message for computer's choice
    print "Computer chooses " + comp_choice
    
    # compute difference of comp_number and player_number modulo five
    num = ( comp_number - player_number ) % 5 
    
    # use if/elif/else to determine winner, print winner message
    if (num == 1) or (num == 2):
        print "Computer wins!"
    elif (num == 3) or (num == 4):
        print "Player wins!"
    else:
        print "Computer and Player tie!"
    
# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")




