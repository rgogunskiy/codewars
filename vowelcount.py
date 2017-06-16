#!/usr/bin/env python3
# Return the number (count) of vowels in the given string.
# We will consider a, e, i, o, and u as vowels for this Kata.


def getCount(inputStr):
    num_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    # your code here
    vovels_in_input = list(filter(lambda x: x in vowels, inputStr))
    num_vowels = len(vovels_in_input)
    return num_vowels

getCount("abracadabra")