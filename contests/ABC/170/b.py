#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    x, y = map(int, input().split())
    if y % 2 != 0:
        print('No')
    elif y // 2 - x < 0 or y > 4 * x:
        print('No')
    else:
        print('Yes')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
