#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from math import atan, degrees


def main():
    input = stdin.buffer.readline
    a, b, x = map(int, input().split())

    if a ** 2 * b > 2 * x:
        h = 2 * x / (a * b)
        print(degrees(atan(b / h)))
    else:
        h = 2 * (a ** 2 * b - x) / (a ** 2)
        print(degrees(atan(h / a)))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
