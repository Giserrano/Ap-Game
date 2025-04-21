import random
from cards import loteria_dict

#Greet user
print("""
      Hello player, welcome to the game of Loteria!
      """)

#translate and track score
def main(loteria_dict):
    correct_answer = 0
    wrong_answer = 0
    need_work = []
    for key in loteria_dict:
        translation = input(f"What does {key} mean?: ")
        capitalized_translation = translation.title()
        print(capitalized_translation)
        if capitalized_translation == loteria_dict[key]:
            print("Correct")
            correct_answer += 1
            print(f"{correct_answer} correct.")
        else: 
            print(f"Incorrect, it means {loteria_dict[key]}")
            wrong_answer += 1
            print(f"{wrong_answer} wrong.")
            need_work.append(key)
        spaced_repitition(need_work)

def spaced_repitition(?):
    user_choice = input("Do you want to practice spaced repitition?: Y/N")
    if user_choice == "N":
        print("Thanks for playing!")
        return
    elif user_choice == "Y":
        for i in wrong_answer:
            print(f"What does {key} mean?: ")


if __name__== "__main__":
    main(loteria_dict)

