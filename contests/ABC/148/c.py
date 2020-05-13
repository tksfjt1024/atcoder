#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def gcd(x, y):
    if x % y == 0:
        return y
    return gcd(y, x % y)


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
