#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    n = int(input())
    a = list(map(int, input().split()))

    c0 = 0
    c4 = 0

    for ai in a:
        if ai % 2 != 0:
            c0 += 1
        if ai % 4 == 0:
            c4 += 1
    if c0 + c4 == n and c0 == c4 + 1:
        print('Yes')
    elif c0 > c4:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
