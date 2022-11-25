"""
File: hailstone.py
Name:洪筠筑
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This program is used to solve the Hailstone Sequence and statistic how many steps it take.
    """
    x = 0
    n = int(input('Enter the number: '))
    if n == 1:
        print("It took 0 steps to reach 1.")
    else:
        while n != 1:
            if n % 2 != 0:
                print(str(int(n))+" is odd, so I make 3*n+1:"+str(int(3 * n + 1)))
                n = 3 * n + 1
                x += 1
            else:
                print(str(int(n))+" is even, so I take half:" + str(int(n / 2)))
                n = n / 2
                x += 1
        print("It took "+str(x)+" steps to reach 1.")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
