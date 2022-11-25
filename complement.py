"""
File: complement.py
Name:洪筠筑
----------------------------
This program uses string manipulation to
tackle a real world problem - finding the
complement strand of a DNA sequence.
THe program asks uses for a DNA sequence as
a python string that is case-insensitive.
Your job is to output the complement of it.
"""


def main():
    """
    This function is used to illustrate the complement of the DNA.
    """
    s = input("Please give me a DNA strand and I'll find the complement: ")
    build_complement(s)
    print("The complement of "+str(s)+" is "+str(build_complement(s)))


def build_complement(s):
    big = my_bigger(s)
    ans = complement(big)
    return ans


def my_bigger(s):
    """
    :param s:str
    :return: str,upper
    """
    big=""
    for i in range(len(s)):
        bigger=s[i]
        if bigger.islower():
            big += bigger.upper()
        else:
            big += bigger
    return big

def complement(big):
    """
    :param big: str
    :return: str,complement
    """
    ans =""
    for i in range(len(big)):
        new = big[i]
        if new == 'A':
            ans += 'T'
        elif new == 'T':
            ans += 'A'
        elif new == 'C':
            ans += 'G'
        elif new == 'G':
            ans += 'C'
    return ans



# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
