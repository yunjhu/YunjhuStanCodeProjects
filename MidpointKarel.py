"""
File: MidpointKarel.py
Name:洪筠筑Ashley
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *


def main():
    """
    pre-condition:Karel is on the street1, avenue1, facing East.
    post-condition:Karel is on the middle of the street1.
    """
    put_beeper()
    if front_is_clear():
        move()
        if front_is_clear():
            find_the_midpoint()
            pick_unnecessary_beeper()
            move_to_the_midpoint()
        else:
            turn_around()
            move_to_the_midpoint()
    pick_beeper()
    put_beeper()


def find_the_midpoint():
    """
    pre-condition:Karel is on the street1, avenue1, facing East.
    post-condition:Karel is on the midpoint with all beepers.
    """
    place_beeper_beside_wall()
    while not on_beeper():
        move()
        if on_beeper():
            turn_around()
            move()
            put_beeper()
        if not on_beeper():
            while not on_beeper():
                move()
            turn_around()
            move()
            put_beeper()
            move()


def place_beeper_beside_wall():
    while front_is_clear():
        move()
    put_beeper()
    turn_around()
    move()


def turn_around():
    turn_left()
    turn_left()


def pick_unnecessary_beeper():
    """
    pre-condition:Karel is on the midpoint with all beepers.
    post-condition:Karel have picked all unnecessary beepers,beside the wall.
    """
    while front_is_clear():
        move()
        pick_beeper()
    turn_around()
    while not on_beeper():
        move()
    while front_is_clear():
        move()
        pick_beeper()
    turn_around()


def move_to_the_midpoint():
    while not on_beeper():
        move()

# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
