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

# Your code here