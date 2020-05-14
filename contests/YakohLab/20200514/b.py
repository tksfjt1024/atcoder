#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
import math


def main():
    input = stdin.buffer.readline
    a, b, x = map(int, input().split())
    v = (a ** 2) * b

    if 0.5 * v > x:
        h = x * 2 / (a * b)
        ans = b / h
    else:
        diff = v - x
        h = (diff * 2 / (a ** 2))
        ans = h / a
    print(math.degrees(math.atan(ans)))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
