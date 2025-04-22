import random
from cards import loteria_dict

#chatgpt
words = list(loteria_dict.items())
random.shuffle(words)

renamed_dict = dict(words)

#Greet user
print(f"""
      Hello player, welcome to the game of Loteria! Here are the card named: {renamed_dict}
      """)
print(renamed_dict)

#translate and track score
def main(loteria_dict):
    loteria_dict = renamed_dict
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
            print()
        retry_words(need_work)


def retry_words(need_work):
    if not need_work:
        print("No words to review, congrats!")
        return
    
    user_choice = input("Do you want to practice the words you missed?: Y/N")
    if user_choice == "N":
        print("Thanks for playing!")
        return
    
    elif user_choice == "Y":
        retry_words(need_work)
            
    else:
        print("Invalid Answer")

def retry_questions(need_work):
    loteria_dict = renamed_dict

    for key in need_work:
        response = input(f"What does {key} mean?: ")
        
        if 



if __name__== "__main__":
    main(loteria_dict)

