"""
File: anagram.py
Name: Ashley
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    This program can be used to find the anagrams.
    """
    start = time.time()
    print('Welcome to stanCode \"Anagram Generator\" (or -1 to quit)')
    read_dictionary()
    sth = input('Find anagrams for:')
    ans = find_anagrams(sth)
    print(ans)
    print(f'{len(ans)} anagrams: {ans}')
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    dic = []
    with open(FILE,'r') as f:
        for line in f:
            word = line.strip()
            dic.append(word)
    return dic


def find_anagrams(s):
    ans_lst = []
    lst = read_dictionary()
    find_anagrams_helper(s, '', ans_lst)
    return ans_lst


def find_anagrams_helper(s, current_s, ans_lst):
    """
    :param : s is the word, current_s is a str with current situation
    ,ans_lst is a list with anagrams, dictionary_list is a list with all of the word.
    :return: anagrams
    """
    dictionary = read_dictionary()
    if len(s) == 0:                                 # 2. Base Case
        if current_s not in ans_lst:
            if current_s in dictionary:
                ans_lst.append(current_s)
                print('Found:', current_s)
                print('Searching...')

    else:                                           # 1. Recursive Case
        for i in range(len(s)):
            # Choose
            current_s += s[i]
            unused_s = s[0:i]+s[i+1:]
            # Explore
            if has_prefix(current_s):
                find_anagrams_helper(unused_s, current_s, ans_lst)
            # Un-choose
            current_s = current_s[:-1]


def has_prefix(sub_s):
    dictionary = read_dictionary()
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
