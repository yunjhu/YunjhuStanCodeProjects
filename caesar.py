"""
File: caesar.py
Name:洪筠筑
------------------------------
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    """
    This program helps to decipher the Caesar.
    """
    secret_number = int(input('Secret number； '))
    s = input("What's the ciphered string?")
    first_part = ALPHABET[26 - secret_number:]
    second_part = ALPHABET[:26 - secret_number]
    new_alp = first_part + second_part
    big = my_bigger(s)
    ans = ""
    for i in range(len(big)):
        if big[i].isalpha():
            x = 0
            while True:
                if big[i] == new_alp[x]:
                    ans += ALPHABET[x]
                    break
                x += 1
        else:
            ans += big[i]
    print("The deciphered string is: "+str(ans))


def my_bigger(s):
    big = ""
    for box in s:
        if box.isupper():
            big += box
        else:
            big += box.upper()
    return big






# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
