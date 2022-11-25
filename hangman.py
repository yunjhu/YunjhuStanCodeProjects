"""
File: hangman.py
Name:洪筠筑
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
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
    This program could be used to play hangman.
    """
    ran = random_word()
    dash = dashed(ran)
    print('The word looks like '+str(dash))
    print('You have '+str(N_TURNS)+' wrong guesses left')
    s = input('Your guess: ')
    big_s = my_bigger(s)
    now = dashed(ran)
    now_life = N_TURNS
    while now.find('-') != -1:
        if now_life == 0:
            break
        else:
            if big_s in ran:
                ans = ""
                for i in range(len(ran)):
                    alp = ran[i]
                    if alp != big_s:
                        ans += now[i]
                    else:
                        ans += big_s
                now = ans
                print('You are correct!')
                if now.find('-') != -1:
                    print('The word looks like '+str(now))
                    print('You have ' + str(now_life) + ' wrong guesses left.')
                    s = input('Your guess:')
                    big_s = my_bigger(s)
                else:
                    print('You win!')
                    print('The word was: ' + str(ran))
            else:
                #guess wrong
                now_life -= 1
                print('There is no '+str(big_s)+"'s"+' in the word.')
                if now_life != 0:
                    print('The word looks like '+str(now))
                    print('You have '+str(now_life)+' wrong guesses left.')
                    s = input('Your guess:')
                    big_s = my_bigger(s)
                else:
                    print('You are completely hung :(')
                    print('The word was: ' + str(ran))

def dashed(ran):
    ans = ""
    for i in range(len(ran)):
        ans += '-'
    return ans

def my_bigger(s):
    if s.isupper():
        return s
    else:
        big_s = s.upper()
        return big_s


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
