#!/usr/bin/env python3

from sys import stdin, setrecursionlimit
from decimal import Decimal


def main():
    input = stdin.readline
    a, b = map(str, input().split())
    a = Decimal(a)
    b = Decimal(b)
    print(int(a * b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
