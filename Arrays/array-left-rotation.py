#!/bin/python3

import os
import sys
import collections

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    nd = collections.deque(a);
    nd.rotate(-d)
    print (*list(nd))