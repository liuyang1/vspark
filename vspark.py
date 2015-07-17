#! /usr/bin/env python2
#-*- encoding=utf8 -*-
import sys
import os
import math

low, high = 0, 200 * 1000
tbl = u" ▏▎▍▌▋▊▉█"
# tbl = "0123456789"


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
    z = int(z)
    y = int(y)
    return tbl[8] * (z) + tbl[(y)]


if __name__ == "__main__":
    width = getTermWidth()
    for v in iter(sys.stdin.readline, ''):
        v = int(v)
        s = mapBar(v, low, high, width)
        print(s)
