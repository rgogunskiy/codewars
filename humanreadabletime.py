#!/usr/bin/env python3

# Write a function, which takes a non-negative integer (seconds) as input
# and returns the time in a human-readable format (HH:MM:SS)
#
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)

import time
def make_readable(seconds):
    # Do something
    gm_time = time.gmtime(seconds)
    days = int(time.strftime("%d",gm_time))
    result = time.strftime("%H:%M:%S", time.gmtime(seconds))
    if days > 1:
        t = (days - 1) * 24 + int(result[0:2])
        result = str(t) + result[2:]
    return result

print(make_readable(359999))

# def make_readable2(s):
#     return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)
#
# print(make_readable2(359999))

def make_readable3(seconds):
    hours, seconds = divmod(seconds, 60 ** 2)
    minutes, seconds = divmod(seconds, 60)
    return '{:02}:{:02}:{:02}'.format(hours, minutes, seconds)

print(make_readable3(359999))