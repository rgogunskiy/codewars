#!/usr/bin/env python3

# Write a reverseWords function that accepts a string a parameter, 
# and reverses each word in the string. Every space should stay, 
# so you cannot use words from Prelude.
# Example:
# reverseWords("This is an example!"); // returns  "sihT si na !elpmaxe"

def reverse_words(str):
    tmp = str.split(' ')
    return ' '.join(tmp[i][::-1] for i in range(len(tmp)))
    #return str

print(reverse_words("This is an example!"))
print(reverse_words('elbuod  decaps sdrow'))