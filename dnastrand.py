#!/usr/bin/env python3
# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
# If you want to know more http://en.wikipedia.org/wiki/DNA
# In DNA strings, symbols "A" and "T" are complements of each other,
# as "C" and "G". You have function with one side of the DNA (string,
# except for Haskell); you need to get the other complementary side.
# DNA strand is never empty or there is no DNA at all (again, except for Haskell).Haskell

def DNA_strand(dna):
    result = ''
    for sym in dna:
        if sym == 'A':
            result += 'T'
        elif sym == 'T':
            result += 'A'
        elif sym == 'C':
            result += 'G'
        elif sym == 'G':
            result += 'C'
    return result

def DNS_strand2(dna):
    return dna.translate(str.maketrans('ATCG', 'TAGC'))


print(DNA_strand('ATTGC'))
print(DNS_strand2('ATTGC'))