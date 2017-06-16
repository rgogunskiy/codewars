#!/usr/bin/env python3
# Usually when you buy something, you're asked whether your credit card number,
# phone number or answer to your most secret question is still correct.
# However, since someone could look over your shoulder, you don't want
# that shown on your screen. Instead, we mask it.

# Your task is to write a function maskify, which changes all
# but the last four characters into '#'.

# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    result = '#' * (len(cc)-4) + cc[-4:]
    return result

print(maskify('5sdf'))
print(maskify('12345678'))