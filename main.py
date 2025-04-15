import random
from cards import dictionary_cards

#Greet user
print("""
      Hello player, welcome to the game of Loteria! 
      Here are the rules of the game: 
        1st, Choose a big card, 
        2nd-shuffle the deck of cards,
        3rd-either the computer or the user picks a card from the deck of cards, 
        4th- If the card someone pulls is on your big card, cover it with a bean, 
        5th- repeat until someone has 4 in a row horizontally or diagonally on their card. 
        Lastly, if the user can choose to continue the round utnil either the computer or user gets a blackout
      """)

#Randomize big cards
#i want to randomize 10 different big cards with only 16 keys from dictionary in a 4x4 format
def randomize_cards(dictionary_cards):
    keys = list(dictionary_cards.keys())
    random.shuffle(keys) 
    #code from gemini AI(lines 22-23)
    for i in range(16):
        print(keys[i])
        print(f"""
    {1}, {2}, {3}, {4}

    {5}, {6}, {7}, {8}

    {9}, {10},{11},{12}

    {13},{14},{15},{16}     
""")
    return keys

#choose a big card


randomize_cards(dictionary_cards)