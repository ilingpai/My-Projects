"""
File: hangman.py
Name:
-----------------------------
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    """
    find the word
    """
    s = random_word()  # s = answer
    ch = ""  # ch = --------
    for i in range(len(s)):
        ch += '-'
    print("The word looks like:" + ch)  # before guessing we have to know the answer.
    print(s)
    guesses(s, ch)  # p = user enter the right letter, and ch shows the letter
    remain_turns = N_TURNS


def guesses(s, ch):
    remain_turns = N_TURNS
    answer = ch
    while remain_turns > 0:
        if answer != s:  # while not find the answer yet
            result = str(input("Your guess: ")).upper()
        if not result.isalpha():  # if user enter a number or letters
            print("illegal format.")
        else:
            if s.find(result) != -1:
                print("You are correct!")
                new_answer=""
                for i in range(len(s)):  # find the letter and update the answer
                    if s[i] == result:
                        new_answer += result
                    else:
                        new_answer += answer[i]
                answer = new_answer
                if answer == s:
                    print("You win !")
                    print("The answer is: " + s)
                    return
            elif s.find(result) == -1:
                remain_turns -= 1
                print("There's no " + result + "'s in the world.")
            print("The word looks like:" + str(answer))
            print("You have " + str(remain_turns) + " wrong guess left.")

    print("You are completely hung :(")
    print("The answer is:" + s)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
