"""
File: class_reviews.py
Name:洪筠筑
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'


def main():
    """
    This program helps to calculate the performance of the final exam.
    """
    class_name = input('Which class? ')
    class_name = class_name.upper()
    how_many_001score = 0
    how_many_101score = 0
    if class_name == EXIT:
        print('No class scores were entered')
    else:
        score = int(input('Score: '))
        if class_name == 'SC001':
            max001 = score
            min001 = score
            total001 = score
            how_many_001score = 1
            max101 = 0
            min101 = 100
            total101 = 0
        else:
            max101 = score
            min101 = score
            total101 = score
            how_many_101score = 1
            max001 = 0
            min001 = 100
            total001 = 0
        while True:
            class_name = input('Which class? ')
            if class_name == EXIT:
                print('=============SC001=============')
                if how_many_001score == 0:
                    print('No score for SC001')
                else:
                    print('Max (001):' + str(max001))
                    print('Min (001):' + str(min001))
                    print('Avg (001):' + str(total001 / how_many_001score))
                print('=============SC101=============')
                if how_many_101score == 0:
                    print('No score for SC101')
                else:
                    print('Max (101):' + str(max101))
                    print('Min (101):' + str(min101))
                    print('Avg (101):' + str(total101 / how_many_101score))
                break
            elif class_name == 'SC001':
                score = int(input('Score: '))
                if score > max001:
                    max001 = score
                if score < min001:
                    min001 = score
                total001 += score
                how_many_001score += 1
            elif class_name == 'SC101':
                score = int(input('Score: '))
                if score > max101:
                    max101 = score
                if score < min101:
                    min101 = score
                total101 += score
                how_many_101score += 1


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
