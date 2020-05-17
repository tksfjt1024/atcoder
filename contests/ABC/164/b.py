#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b, c, d = map(int, input().split())
    while True:
        c -= b
        if c <= 0:
            print('Yes')
            break
        a -= d
        if a <= 0:
            print('No')
            break


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
