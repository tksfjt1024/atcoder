#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from math import radians, cos


def main():
    input = stdin.buffer.readline
    a, b, h, m = map(int, input().split())

    d_h = 360 * (h + m / 60) / 12
    d_m = 360 * m / 60

    d = abs(radians(d_h - d_m))

    print((a ** 2 + b ** 2 - 2 * a * b * cos(d)) ** 0.5)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
