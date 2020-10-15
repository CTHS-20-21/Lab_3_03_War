# War starter code ##############

import random

# name: shuffled_deck
# purpose: will return a shuffled deck to the user
# input:
# returns: a list representing a shuffled deck
def shuffled_deck():
    basic_deck = list(range(2, 15)) * 4
    random.shuffle(basic_deck)
    return basic_deck

deck = shuffled_deck()
print("The starter deck looks like this:\n" + str(deck)) # delete this line of code in your final lab submission

#################################

# Your code here (write the functions below, and complete the rest of the game)


# Write the function based on the contract
# name: player_turn
# purpose: takes in a player name and draws/removes a card from the deck, prints "user drew card x", and returns the value
# Arguments: player_name as string, deck as list
# returns: integer


# Finish the contract and write the function based on the contract
# name: compare_scores (Write your own contract!)
# purpose:
# Arguments:
# returns:


