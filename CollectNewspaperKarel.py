"""
File: CollectNewspaperKarel.py
Name:洪筠筑Ashley
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is in the upper left corner of the house without newspaper, facing East.
    post-condition:Karel is in the upper left corner of the house with newspaper, facing East.
    """
    move_to_paper()
    take_paper_into_home()


def move_to_paper():
    move()
    move()
    turn_right()
    move()
    turn_left()
    move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def take_paper_into_home():
    pick_beeper()
    turn_around()
    move()
    turn_right()
    move()
    turn_left()
    move()
    move()
    turn_around()
    put_beeper()


def turn_around():
    turn_left()
    turn_left()



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
