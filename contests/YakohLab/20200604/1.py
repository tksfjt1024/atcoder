#!/usr/bin/env python3

from sys import stdin, setrecursionlimit


def main():
    input = stdin.buffer.readline
    abc = map(int, input().split())
    a, b, c = sorted(abc)
    if (b - a) % 2 == 0:
        print((2 * c - a - b) // 2)
    else:
        print((2 * (c + 1) - a - b - 1) // 2 + 1)


if __name__ == "__main__":
    setrecursionlimit(10000)
    main()
