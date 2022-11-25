"""
File: StoneMasonKarel.py
Name:洪筠筑Ashley
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on the street1, avenue1, facing East.
    post-condition:Karel is on the last avenue, 1st Street, facing east.
    """
    if not on_beeper():
        put_beeper()
    turn_left()
    while right_is_clear():
        up()
        if right_is_clear():
            cross_up()
            down()
        else:
            for i in range(4):
                move()
                turn_left()
        if front_is_clear():
            cross_down()


def up():
    """
    pre-condition:Karel is under the broken column, facing North.
    post-condition:Karel is on the sound column, facing East.
    """
    while not on_beeper():
        put_beeper()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    if not on_beeper():
        put_beeper()
    turn_right()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def cross_up():
    """
    pre-condition:Karel is on the sound column, facing East.
    post-condition:Karel is on the broken column, facing South.
    """
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    turn_right()
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_left()
    move()
    # for i in range(4):
    #     move()
    turn_right()


def down():
    """
    pre-condition:Karel is on the broken column, facing South.
    post-condition:Karel is under the sound column, facing East.
    """
    while not on_beeper():
        put_beeper()
    while front_is_clear():
        if not on_beeper():
            put_beeper()
            move()
        else:
            move()
    turn_left()


def cross_down():
    """
    pre-condition:Karel is under the sound column, facing East.
    post-condition:Karel is under the broken column, facing North.
    """
    for i in range(4):
        move()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
