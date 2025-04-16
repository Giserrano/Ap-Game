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
    print(keys)

def big_cards(dictionary_cards):
        card_one = print(f"""
            Card 1
    {dictionary_cards[7]},  {dictionary_cards[22]}, {dictionary_cards[38]},  {dictionary_cards[4]},

    {dictionary_cards[29]}, {dictionary_cards[50]}, {dictionary_cards[11]}, {dictionary_cards[33]},

    {dictionary_cards[15]}, {dictionary_cards[41]},  {dictionary_cards[2]}, {dictionary_cards[45]},

    {dictionary_cards[18]}, {dictionary_cards[53]}, {dictionary_cards[25]},  {dictionary_cards[9]},    
""")
        card_two = print(f"""
            Card 2
     {dictionary_cards[5]}, {dictionary_cards[28]}, {dictionary_cards[46]},  {dictionary_cards[8]},

    {dictionary_cards[31]}, {dictionary_cards[16]}, {dictionary_cards[43]}, {dictionary_cards[10]},

    {dictionary_cards[12]}, {dictionary_cards[49]}, {dictionary_cards[20]}, {34},

     {6}, {51}, {23}, {13},  
    """)
        card_three = print(f"""
            Card 3
     {3}, {30}, {47},  {1},

    {21}, {36}, {17}, {52},

    {24}, {44}, {35}, {19},

    {32}, {48}, {14}, {26},  
    """)
        card_four = (f"""
            Card 4
    {27}, {42}, {37}, {40},

    {53}, {18}, {33}, {11},

     {4}, {29}, {25},  {5},

    {50},  {9}, {12},  {8},  
    """)


def choose_card():
    card_list = [card_one, card_two,card_three,card_four]
    choose_bigcard = input(f"Which card do you want? 1, 2, 3, or 4: ")
    if choose_bigcard == "1":
        print(f"Your card is {card_one}")
    elif choose_bigcard == "2":   
        print(f"Your card is {}")
    elif choose_bigcard == "3":
        print(f"Your card is {}")
    elif choose_bigcard == "4":
        print(f"Your card is {}")

randomize_cards(dictionary_cards)
big_cards()

