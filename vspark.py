#! /usr/bin/env python3
#-*- encoding=utf8 -*-
import sys
import os
import math

tbl = " ▏▎▍▌▋▊▉█"
# tbl = "0123456789"

low, high = 0, 200


def getTermWidth():
    v = os.popen('tput cols').read()
    return int(v)


def trans(v, low, high, width):
    """
    >>> trans(100, 0, 200, 10)
    (5, 0)
    >>> trans(50, 0, 200, 10)
    (2, 4)
    >>> trans(25.4, 0, 200, 10)
    (1, 2)
    """
    r = (high - low) / width
    r = math.ceil(r)
    z = v // r
    y = (v % r) * 8 // r
    return (math.ceil(z), math.ceil(y))


def mapBar(v, low, high, width):
    z, y = trans(v, low, high, width)
    # print(z, y)
    return tbl[8] * (z) + tbl[(y)]


if __name__ == "__main__":
    width = getTermWidth()
    while 1:
        try:
            v = input()
        except EOFError:
            break
        v = int(v)
        # print(v)
        s = mapBar(v, low, high, width)
        print(s)
