import random
from cards import loteria_dict

#Greet user
print("""
      Hello player, welcome to the game of Loteria!
      """)

#translate
def main(loteria_dict):
    for key in loteria_dict:
        translation = input(f"What does {key} mean?: ")
        capitalized_translation = translation.title()
        print(capitalized_translation)
        if capitalized_translation == loteria_dict[key]:
            print("Correct")
        else: 
            print(f"Incorrect, it means {loteria_dict[key]}")

    


main(loteria_dict)
#Randomize big cards
# def randomize_cards(dictionary_cards):
#     keys = list(dictionary_cards.keys())
#     random.shuffle(keys) 
#     print(keys)
