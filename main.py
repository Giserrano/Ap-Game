import random
from cards import loteria_dict

#chatgpt on lines 5-8
words = list(loteria_dict.items())
random.shuffle(words)

renamed_dict = dict(words)

#Greet user
print(f"""
      Hello player, welcome to the game of Loteria! I'm going to prompt a word in spanish and you have to translate it. 
      """)

#translate and track score
def main(loteria_dict):
    loteria_dict = renamed_dict
    correct_answer = 0
    wrong_answer = 0
    need_work = []
    ques_num = 1
    for key in loteria_dict:
        translation = input(f"What does {key} mean?: ")
        capitalized_translation = translation.title()
        if capitalized_translation == loteria_dict[key]:
            print(f"Number {ques_num}, CORRECT!")
            correct_answer += 1
            ques_num += 1
            print(f"So far you have {correct_answer} correct.")
        elif capitalized_translation != "":
            #something here
        elif capitalized_translation != loteria_dict[key]:
            print(f"Number {ques_num} INCORRECT, it means {loteria_dict[key]}")
            wrong_answer += 1
            ques_num += 1
            print(f"{wrong_answer} wrong.")
            need_work.append(key)
    retry_words(need_work)

def retry_words(need_work):
    if not need_work:
        print("No words to review, congrats!")
        return
    
    user_choice = input("Do you want to practice the words you missed?: Y/N: ")
    cap_choice = user_choice.title()
    if cap_choice == "N":
        print("Thanks for playing!")
        return
    
    elif cap_choice == "Y":
        retry_questions(need_work)
            
    else:
        print("Invalid Answer")

def retry_questions(need_work):
    loteria_dict = renamed_dict
    wrong_answer = 0
    correct_answer = 0

    for key in need_work:
        response = input(f"What does {key} mean?: ")
        cap_response = response.title()
        
        if cap_response == loteria_dict[key]:
            print("Correct")
            correct_answer += 1
            print(f"{correct_answer} correct.")
        else: 
            print(f"Incorrect, it means {loteria_dict[key]}")
            wrong_answer += 1
            print(f"{wrong_answer} wrong.") 
    print("Thanks for playing, I hope you learned some spanish.")



if __name__== "__main__":
    main(loteria_dict)

