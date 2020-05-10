#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, c, k = map(int, input().split())
    if k <= a:
        print(k)
    elif a < k <= a + b:
        print(a)
    elif a + b < k:
        print(a - (k - a - b))


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
