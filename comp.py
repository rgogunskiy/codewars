#!/usr/bin/env python3
# Given two arrays a and b write a function comp(a, b) (compSame(a, b) in Clojure)
# that checks whether the two arrays have the "same" elements, with the same multiplicities.
# "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
# Examples
# Valid arrays
# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
# comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the square of 144,
# 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write b's elements
# in terms of squares:

# a = [121, 144, 19, 161, 19, 144, 19, 11]
# b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]


def comp(array1, array2):
    if (array1 is None) or (array2 is None) or (not array1) or (not array2):
        return False

    result = True
    for x in array1:
        if x ** 2 not in array2:
            result = False
            break
    return result

a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a, b))
