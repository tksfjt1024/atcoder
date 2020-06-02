#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    a, b = map(int, input().split())
    if (a + b) % 2 == 0:
        print((a + b) // 2)
    else:
        print('IMPOSSIBLE')


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
