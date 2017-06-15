#!/usr/bin/env python3

# Welcome. In this kata, you are asked to square every digit of a number.
# For example, if we run 9119 through the function, 811181 will come out.
# Note: The function accepts an integer and returns an integer


def square_digits(num):
    num = str(num)
    result = ''
    for digit in num:
        digit = int(digit)
        result += str(digit ** 2)
    return int(result)


print(square_digits(9119))
