"""
File: CheckerboardKarel.py
Name:洪筠筑Ashley
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on the street1, avenue1, facing East.
    post-condition:Karel finished its work.
    """
    while front_is_clear():
        fill_one_line()
        turn_left()
        if front_is_clear():
            if on_beeper():
                move()
                turn_left()
                if front_is_clear():
                    move()
                    fill_one_line()
            else:
                move()
                turn_left()
            if front_is_clear():
                fill_one_line()
            turn_right()
            if front_is_clear():
                move()
                turn_right()


def fill_one_line():
    """
        pre-condition:Karel is on the new and empty line, ready to do it, facing the line.
        post-condition:Karel finished one-line work, facing the wall.
    """
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
