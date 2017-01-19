"""
Magic 8 Ball

Welcome to the magic 8 Ball

Type Play or Exit:

Loop Play (While Play == True, else Exit)

"""
import random


def magic_8_ball():
    answer_key = {1:'This is not your day',
                  2:'You could be onto something',
                  3:'I\'m doubtful',
                  4:'Your wish will come true',
                  5:'Not going to happen Capt',
                  6:'Are you kidding me?'}

    answering = True
    while answering:
        question = input("Welcome to Magic 8 Ball, What is your question or wish? : ")

        choice = random.randint(1, len(answer_key))

        print(answer_key[choice])

        response = input("Do you want to add an answer for this round? 'y/n'? : ")

        if response == 'y':
            answer_key.update({len(answer_key)+1: input("What is the new answer you would like added? : ")})

        elif response == 'n':
            ask_another_question = input("Would you like to ask another question or exit? 'y/exit': ")

            if ask_another_question == 'y':
                continue

            elif ask_another_question == 'exit':
                print("Thank you for playing... Come again!")
                exit()

magic_8_ball()
